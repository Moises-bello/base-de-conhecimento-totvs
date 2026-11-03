---
content_hash: 893a600fd2b85608266390e2579bb9cb746bd910bc5a716c063f2dad324b72da
fetched_at: '2026-06-29T00:05:54.697357+00:00'
page_id: '1080895382'
product: rm
source: tdn-rm
title: AGENTE IA - Gestor 360º
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1080895382
version: 1
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Telas utilizadas**

Identificação PEPVisão Geral

## **01. VISÃO GERAL**

O Agente de Inteligência Assistencial desenvolvido na plataforma LYNN atua como uma camada supervisora autônoma sobre o Prontuário Eletrônico do Paciente (PEP). Seu principal objetivo de negócio é mitigar riscos hospitalares, otimizar o dimensionamento de pessoal e fornecer à alta gestão uma visão consolidada e em tempo real da operação assistencial.

Para o cliente (diretoria, gerência de enfermagem e qualidade), o valor real da solução LYNN reside nos seguintes pilares:

* O subagente de protocolos e interconsultas serve como um farol de riscos. Saber que um protocolo de Sepse está aberto e sem desfecho há horas permite uma intervenção proativa antes que o quadro do paciente piore ou gere inconformidade de auditoria. Interconsultas pendentes que podem ser gargalos para alta hospitalar ou decisão clínica.
* O relatório consolidado Visão 360o unifica visões que normalmente exigiriam que o gestor abrisse dezenas de telas diferentes no ERP, poupando tempo operacional crítico.
* Através da análise automatizada do Score de Fugulin, o gestor sabe exatamente quais setores demandam mais técnicos e enfermeiros por turno, garantindo conformidade com as exigências legais do COFEN sem sobrecarregar a equipe.

Ao automatizar o desenho do cenário clínico e o cálculo de dimensionamento antes de cada plantão, o agente elimina as etapas burocráticas invisíveis que geram sobrecarga, permitindo que o profissional de saúde saia de trás das telas de computador e volte a focar sua energia e vocação onde elas realmente importam: à beira do leito, cuidando e olhando para o ser humano de verdade.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

O agente principal funciona como uma central de triagem inteligente e de alta autonomia, projetada para eliminar o trabalho manual de auditoria e compilação de dados. Acionado de forma invisível e automática antes de cada troca de plantão, o sistema ativa seus cinco subagentes integrados para desenhar o retrato exato da unidade. Ele correlaciona o preenchimento do score de Fugulin com a complexidade clínica real dos leitos, entregando ao tomador de decisão o cálculo matemático imediato do contingente de profissionais necessário para o período, transformando dados complexos em uma escala equilibrada e seguindo a legislação do COFEN.

| **Subagente (ID Técnico)** | **Função de Negócio (O que faz?)** |
| --- | --- |
| **agente\_censo\_hospitalar** | Realiza a leitura do censo diário do setor, calculando indicadores de ocupação, leitos ativos, taxas de permanência média e mapeamento de altas previstas. |
| **agente\_isolamento** | Identifica e lista em tempo real os pacientes internados sob regime de isolamento ativo ou precauções específicas (contato, gotículas, aerossóis), cruzando dados de infecção com o mapa de leitos. |
| **agente\_protocolo** | Rastreia linhas de cuidado e identifica criticidades em protocolos clínicos abertos e em andamento (ex: Sepse, AVC, IAM, Dor Torácica), apontando o tempo decorrido desde a abertura. |
| **agente\_interconsulta** | Varre o painel de pareceres médicos e exibe de forma detalhada o status das interconsultas solicitadas a especialidades, destacando os pedidos pendentes e tempos de atraso. |
| **agente\_score** | Avalia a carga assistencial do setor por meio dos scores preenchidos (Fugulin,), aplicando as regras de dimensionamento de enfermagem.  [Resolução Cofen nº 743/2024](https://www.cofen.gov.br/resolucao-cofen-no-743-de-12-de-marco-de-2024/) |

O agente foi projetado sob o princípio de Privacy by Design, em conformidade com a Lei Geral de Proteção de Dados (LGPD - Lei no 13.709/2018), tratando os dados do PEP como dados pessoais sensíveis (Art. 5o, II):

* Em nenhuma hipótese o agente exibe o nome completo do paciente em relatórios visuais, logs textuais expostos ou corpos de e-mail. Os nomes são convertidos para suas iniciais extremas (ex: "Anderson Souza" vira "A. S.").
* Informações de identificação direta desnecessárias para a tomada de decisão gerencial imediata — tais como número de CPF, RG — são integralmente descartadas e suprimidas durante a etapa de tratamento dos subagentes.

O sistema conta com um módulo de distribuição automatizada de relatórios gerenciais pré configurados:

* Disparos Agendados: Os relatórios podem ser configurados para execução automática em horários estratégicos (ex: Passagem de Plantão às 06:00h, 12:00h, 18:00h e 00:00h) ou em fechamentos gerenciais diários.
* Protocolo de Envio: O envio do e-mail é realizado por meio de servidores integrados
* Mecanismo de Rastreabilidade e Entrega: O o agente armazena o status de falha no painel operacional LYNN para auditoria da TI.
