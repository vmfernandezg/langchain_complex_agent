from dotenv import load_dotenv

from agent_app.agent import get_agent_executor, get_tools


def list_capabilities() -> None:
    """Prints the available tools and their descriptions."""
    print("\n" + "=" * 40)
    print("🤖 CAPACIDADES DEL AGENTE")
    print("=" * 40)
    tools = get_tools()
    for tool in tools:
        print(f"🔹 {tool.name}: {tool.description}")
    print("=" * 40 + "\n")


def main() -> None:
    """Main entry point."""
    load_dotenv()
    
    list_capabilities()

    print("Inicializando Agente LangChain (LangGraph)...")
    try:
        graph = get_agent_executor()
        print("Agente inicializado correctamente.")
    except NotImplementedError:
        print(
            "Nota de inicialización: El FakeLLM usado para esta demo no soporta "
            "binding de herramientas."
        )
        print(
            "Para ejecutar con llamadas a herramientas funcionales, por favor "
            "configura una variable de entorno OPENAI_API_KEY válida."
        )
        print(
            "La estructura del proyecto es correcta y lista para "
            "producción con un LLM real."
        )
        return
    except Exception as e:
        print(f"Error inicializando el agente: {e}")
        return

    print("¡Agente listo! Escribe 'salir' o 'terminar' para detener.")
    while True:
        try:
            user_input = input("\nTú: ")
            if user_input.lower() in ["exit", "quit", "salir", "terminar"]:
                print("¡Adiós!")
                break
            
            print("🤔 Agente: Pensando...")
            inputs = {"messages": [("user", user_input)]}
            
            # Use stream to get intermediate steps
            for event in graph.stream(inputs, stream_mode="values"):
                # "values" mode returns the full state at each step
                # We want to see the last message to know what happened
                current_cessages = event.get("messages", [])
                if not current_cessages:
                    continue
                
                last_msg = current_cessages[-1]
                
                # Check for Tool Calls (Agent deciding to act)
                if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
                    for tool_call in last_msg.tool_calls:
                        print(
                            f"  🛠️  Decidiendo usar herramienta: {tool_call['name']} "
                            f"(args: {tool_call['args']})"
                        )
                
                # Check for Tool Outputs (FunctionMessage or ToolMessage)
                # In LangGraph/LangChain, tool outputs are typically ToolMessage
                elif last_msg.type == "tool":
                    print(
                        f"  ✅  Resultado herramienta ({last_msg.name}): "
                        f"{last_msg.content}"
                    )

                # Check for Final Answer (AIMessage without tool calls)
                elif last_msg.type == "ai" and not last_msg.tool_calls:
                    print(f"💬 Agente: {last_msg.content}")
        except Exception as e:
            print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
