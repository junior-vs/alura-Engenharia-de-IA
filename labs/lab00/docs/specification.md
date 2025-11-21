# Especificação do Projeto

## Objetivo

Criar um assistente virtual médico, treinado com os dados próprios do hospital, capaz de auxiliar nas condutas clínicas, responder dúvidas de médicos e sugerir procedimentos com base nos protocolos internos. Além disso, a ideia é organizar fluxos de decisão automatizados e seguros, onde, por exemplo, ao receber informações sobre um paciente, o sistema possa acionar diferentes etapas, como verificar exames pendentes, sugerir tratamentos e emitir alertas para a equipe médica — tudo isso coordenado com LangChain.

## Requisitos obrigatório

1. Fine-tuning de LLM com dados médicos internos
- Realizar o fine-tuning de um modelo LLM (como LLaMA, Falcon ou um outro) utilizando:
- Protocolos médicos do hospital; 
- Exemplos de perguntas frequentes feitas por médicos; 
- Modelos de laudos, receitas e procedimentos internos.
- Preparar os dados com técnicas de preprocessing, anonimização e curadoria

2. Criação de assistente médico com LangChain
- Utilizar o LangChain para:
- Construir um pipeline que integre a LLM customizada;
- Realizar consultas em base de dados estruturadas (como prontuários e registros);
- Contextualizar as respostas da LLM com informações atualizadas
do paciente.

3. Segurança e validação
- Definir os limites de atuação do assistente para evitar sugestões
impróprias (exemplo: nunca prescrever diretamente, sem a
validação humana);
- Implementar logging detalhado para rastreamento e auditoria;
- Garantir explainability das respostas da LLM (exemplo: indicar a fonte
da informação utilizada na resposta).

4. Inteface
- Implementar uma interface para interação com o assistente médico, que permita:
- Realizar consultas em base de dados estruturadas (como prontuários e registros);
- Contextualizar as respostas da LLM com informações atualizadas do paciente.   
- Será utilizado linha de comando
- Será disponibilizado endpoint https restfull para envio de perguntas e mensagem tendo como resposta o texto da resposta da LLM    

## 4. Organização do Código 📦

* **Projeto modularizado em Python:**
    * Estrutura de diretórios clara, separando código-fonte (`src/`), testes (`tests/`), *notebooks* de experimentação (`notebooks/`), e arquivos de configuração/dados.
    * **Separação de responsabilidades** (Classes RAG/Retrieval, Classes de Agentes, Módulos de *Loaders*, etc., em seus próprios arquivos).
* **Instruções completas no `README.md`:**
    * Deve incluir, no mínimo: **instruções de instalação** (dependências, como criar o ambiente), **configuração de variáveis de ambiente** (chaves de API, caminhos de modelos/dados), **como executar** o projeto (treinamento, *inference*, agentes), e **estrutura do projeto**.
* **Uso de `requirements.txt` ou `pyproject.toml`:**
    * Especificar **todas as dependências** do projeto e suas versões (idealmente usando *pinning* de versões para reprodutibilidade).

---

## 5. Padrões de Código e Estilo (Python) 🐍

* **Aderência ao PEP 8:**
    * Utilizar *linters* (ex: **Flake8**, **Pylint**) e formatadores (ex: **Black**, **isort**) para garantir um estilo de código consistente e legível (nomes de variáveis, indentação, limite de linha).
* **Tipagem Estática (Type Hinting):**
    * Utilizar *type hints* (ex: `def func(a: int) -> str:`) em todas as funções e classes para melhorar a **legibilidade**, **manutenibilidade** e permitir a **análise estática** do código.
* **Documentação (*Docstrings*):**
    * Documentar módulos, classes e **todas as funções públicas** usando um padrão reconhecido (ex: **Google**, **Numpy**, ou **Sphinx** style), detalhando parâmetros, tipos de retorno e a função do código.

---

## 6. Programação Orientada a Objetos (POO) e Funcional (FP) 💡

* **POO (LangChain/LangGraph):**
    * **Encapsulamento:** Utilizar classes para agrupar dados e métodos. Exemplo: Uma classe `RAGPipeline` que encapsula o *retriever*, o modelo e a lógica de geração.
    * **Composição sobre Herança:** Favorecer a composição (juntar objetos de outras classes) para criar cadeias complexas de agentes/componentes (princípio fundamental do **LangChain** e **LangGraph**).
* **FP (Geração de Dados/Transformação):**
    * Utilizar funções puras (funções que não causam efeitos colaterais e sempre retornam o mesmo valor para o mesmo *input*) para transformações de dados, pré-processamento de *inputs* e pós-processamento de *outputs*.
    * Minimizar o uso de **estado global** e **mutabilidade**.

---

## 7. Versionamento e Ambiente 💾

* **Versionamento de Código:**
    * Uso de **Git** e seguir o padrão **Git Flow** ou **GitHub Flow**.
    * Utilizar *tags* para marcar versões estáveis (ex: `v1.0.0`) e *releases*.
* **Gerenciamento de Ambiente:**
    * Uso de **Ambientes Virtuais** (ex: `venv`, **Conda**) para isolar dependências.
    * Instruções claras para a recriação do ambiente.
* **Versionamento de Modelos e Dados (MLOps):**
    * Em projetos de **Fine-Tuning** ou **RAG**, usar ferramentas como **DVC (Data Version Control)** ou plataformas MLOps para versionar *datasets*, modelos treinados e configurações de *pipelines*.

---

## 8. Testes e Qualidade de Software ✅

* **Testes Unitários:**
    * Escrever testes unitários para **funções puras** e **componentes individuais** (ex: um componente de **Retrieval** ou uma **Tool** de um agente) usando `pytest`.
* **Testes de Integração:**
    * Testar a **integração** entre os principais componentes (ex: o fluxo completo de um **Agent AI** interagindo com as suas **Tools** ou a cadeia **RAG** completa).
    * Utilizar *mocking* quando necessário para simular APIs externas ou LLMs (que são caros e lentos).
* **Testes de Regressão/Avaliação (ML):**
    * Em **RAG** e **Fine-Tuning**, definir métricas de avaliação (ex: **F1** para extração, **ROUGE** para sumarização, **Context Relevancy** para RAG) e ter um *pipeline* para avaliar o desempenho do modelo em relação a uma *baseline* (modelo anterior).

---

## 9. Segurança e Credenciais 🔑

* **Nunca *commitar* credenciais:**
    * As chaves de API (**OpenAI**, **Hugging Face**, **Banco de Dados**, etc.) devem ser gerenciadas através de **Variáveis de Ambiente** (`os.environ`) ou um serviço de segredos (*secret manager*).
    * Adicionar **padrões de segredos** ao arquivo `.gitignore`.
* **Sanitização de *Inputs*:**
    * Em sistemas de **Agentes** e **RAG**, implementar mecanismos básicos para **validar e sanitizar *inputs*** do usuário antes de passá-los aos LLMs e às *Tools* para mitigar riscos de **Prompt Injection** e ataques de segurança.
'
### Guardrails (Segurança e Qualidade em LLMs/RAG/Agents) 🛡️

Guardrails são camadas de validação e controle proativas que monitoram e restringem tanto as entradas (*inputs*) do usuário quanto as saídas (*outputs*) do modelo de linguagem, garantindo que a operação permaneça dentro dos limites definidos.

#### Guardrails de *Input*
    * **Filtragem de Conteúdo Proibido:** Implementar filtros na entrada para bloquear *prompts* que contenham linguagem abusiva, discurso de ódio, conteúdo ilegal ou solicitação de dados sensíveis (PII).
    * **Defesa contra *Prompt Injection***: Estratégias para detectar e neutralizar comandos maliciosos que tentam desviar o modelo de sua tarefa principal (ex: reescrita de *prompts* ou uso de classificadores de segurança).
    * **Restrição de Escopo:** Limitar o tópico da conversa ou da solicitação à área de atuação do Agente/RAG (ex: bloquear perguntas sobre saúde se o agente for apenas financeiro).

#### Guardrails de *Output*
    * **Verificação de Toxicidade/Conteúdo Inapropriado:** Analisar a resposta gerada pelo LLM antes de exibi-la ao usuário e, se necessário, censurá-la ou substituir por uma mensagem padrão de segurança.
    * **Verificação de Fundamentação (*Grounding* - Crítico para RAG):** Implementar verificações para garantir que a resposta gerada esteja **realmente baseada** nos documentos recuperados pelo RAG, mitigando **alucinações**. *Ferramentas como a própria **LangChain** e a biblioteca **Guardrails AI** (em Python) oferecem validadores para isso.*
    * **Conformidade de Formato:** Garantir que o *output* gerado esteja no formato esperado (ex: JSON estruturado, lista, ou um formato de resposta formal).
    * **Prevenção de Vazamento de PII/Segredos:** Filtrar informações confidenciais ou dados internos da empresa que o modelo possa ter acidentalmente incluído na resposta (ex: *Data Masking*).

#### Guardrails em *Agent AI* (Controle de Ação)
    * **Controle de Uso de *Tools*:** Definir regras estritas sobre quais *Tools* (ferramentas/funções) o Agente pode invocar e com quais parâmetros, garantindo que as ações executadas sejam seguras e dentro do escopo permitido (ex: não permitir que um Agente de suporte realize transferências financeiras).
    * **Limitação de Iterações/Recursos:** Restringir o número de passos/iterações que um Agente pode executar para evitar custos excessivos ou *loops* infinitos (especialmente importante em **LangGraph**).

---


## Datasets

### PubMedQA
Perguntas e respostas clínicas com base em publicações médicas | https://pubmedqa.github.io/

### MedQA-ICD-10
Perguntas e respostas clínicas com base em publicações médicas | https://medqa-icd10.github.io/

