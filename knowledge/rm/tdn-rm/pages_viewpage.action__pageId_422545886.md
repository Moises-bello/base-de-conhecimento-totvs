---
content_hash: d7013e1cd1a6a324cfce55aabf80fef54c9fb9ba63bfed22687ccb9e9510da7b
fetched_at: '2026-06-29T00:09:21.724892+00:00'
page_id: '422545886'
product: rm
source: tdn-rm
title: Emissão da NF-e em Contingência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545886
version: 5
---

O  Sistema  da NF-e é baseado no conceito de documento fiscal eletrônico: um arquivo eletrônico com as informações fiscais da operação comercial que tenha a assinatura digital do emissor.

A validade de uma NF-e está condicionada à existência da respectiva autorização de uso concedida pela Secretaria de Fazenda de localização do emissor ou pelo órgão por  ela designado para autorizar a NF-e em seu nome, como são os casos da SEFAZ Virtual do Ambiente Nacional, da SEFAZ Virtual do Rio Grande do Sul, das Sefaz Virtuais de Contingência (SVC) e do Sistema de Contingência do Ambiente Nacional - SCAN.

A obtenção da autorização de uso da NF-e é um processo que envolve diversos recursos de infraestrutura, hardware e software. O mau funcionamento ou a indisponibilidade de qualquer um destes recursos pode prejudicar o processo de autorização da NF-e, com reflexos nos  negócios do emissor da NF-e que fica impossibilitado de obter a prévia autorização de uso da NF-e exigida na legislação para a emissão do DANFE para acompanhar a circulação da mercadoria.   
A alta disponibilidade é uma das premissas básicas do sistema da NF-e e os sistemas de recepção de NF-e das UF foram construídos para funcionar em regime de 24x7, contudo, existem diversos outros componentes do sistema que podem apresentar falhas e comprometer a disponibilidade dos serviços, exigindo alternativas de emissão da NF-e em contingência.

É aconselhável que os relatórios do DANFE estejam sempre atualizados. Os relatórios podem ser baixados na [página de downloads](http://suporte.totvs.com/download) do suporte.  
Atualmente existem as seguintes modalidades de emissão de NF-e: Normal, FS, FS-DA, EPEC, SVC-RS e SVC-AN, abaixo serão descritas as modalidades que são para utilização em contingência e os detalhes para emissão das notas nas mesmas.

**FS e FS-DA**

Sendo identificada a existência de qualquer incidente que prejudique ou impossibilite a transmissão das NF-e e/ou obtenção da autorização de uso da SEFAZ, a empresa poderá adotar as Contingência FS ou FS-DA sendo que para utilizar a contingência FS o DANFE deverá ser impresso com formulário de segurança.

**Passos para utilização:**  
1 – [Alterar a modalidade de emissão da NF-e](http://tdn.totvs.com/pages/viewpage.action?pageId=422546030) para "Contingência Off-line" (FS) ou "Contingência Off-line FS-DA" (FS-DA);  
2 – Para as NF-e que estão pendentes retorno de autorização da SEFAZ, deverão ser gerados novos movimentos (copias) com novos números para emissão em Contingência;  
3 – Acesse a tela de emissão de NF-e e execute o processo "Gerar DANFE.NET em Contingência" preenchendo os parâmetros necessários na tela do processo;  
4 – Imprima o relatório DANFE clicando no botão "Imprimir DANFE.NET" que ficará disponível na tela de resultado da execução do processo ou selecionando a nota na grid de notas e executando o processo de imprimir o DANFE "Imprimir DANFE.NET (RM Reports)";  
5  – Transmitir as NF-e imediatamente após a cessação dos problemas técnicos que impediam a transmissão da NF-e, observando o prazo limite de transmissão na legislação. Nos casos que foram necessários gerar copias dos movimentos porque as notas estavam com status Pendente as mesmas deverão ser Consultadas e Canceladas ou Inutilizadas conforme cada caso;  
***Observações:***   
1 – O relatório DANFE será impressos a partir das informações constantes no XML da NF-e. Caso após a geração da NF-e em contingência e impressão do relatório seja identificada alguma necessidade de correção, basta corrigir a informação no campo de origem (Cadastros, movimento, etc.), em seguida executar novamente o processo para geração da NF-e em contingência para que o XML da mesma seja atualizado e imprimir o DANFE novamente;  
2 – Ao executar o processo para gerar DANFE em contingência, não serão selecionados Movimentos Cancelados ou movimentos que já estejam com NF-e Pendente, Cancelamento Pendente, Inutilizada, Autorizada, Cancelada ou denegada para geração da DANFE em Contingência;   
3 – Observe se as regras fiscais de contingências definidas no manual da SEFAZ foram respeitadas no DANFE e no XMl da nota.

**SVC-RS e SVC-AN**

Cada SEFAZ poderá ativar a autorização das NF-e através da SVC (SEFAZ Virtual de Contingência) conforme a necessidade, podendo ser por acionamento de emergência ou programado. uma vez ativada a autorização das NF-e passa a ser emitida pela SVC não havendo necessidade de posterior autorização da SEFAZ de origem. Esta modalidade só pode ser utilizada com prévia autorização da SEFAZ.

**Passos para utilização:**  
1 – [Alterar a modalidade de emissão](http://tdn.totvs.com/pages/viewpage.action?pageId=422546030) da NF-e para SVC-AN ou SVC-RS;  
2 – Para as NF-e que estão pendentes retorno de autorização da SEFAZ, deverão ser gerados novos movimentos (copias) com novos números para emissão em Contingência;  
3 – Acesse a tela de emissão de NF-e e execute o processo "Enviar NF-e" normalmente e posteriormente execute a consulta de autorização;  
4 – Imprima o relatório DANFE clicando no botão "Imprimir DANFE.NET" que ficará disponível na tela de resultado da execução do processo ou selecionando a nota na grid de notas e executando o processo de imprimir o DANFE "Imprimir DANFE.NET (RM Reports)";  
5 –Imediatamente após a cessação dos problemas e voltando a normalidade de autorização da NF-e na SEFAZ de origem, deverão ser observados os casos que foram necessários gerar copias dos movimentos porque as notas estavam com status Pendente e as mesmas deverão ser Consultadas e Canceladas ou Inutilizadas conforme cada caso;

Neste caso deve ser verificado junto à SEFAZ de origem qual das duas modalidades deverá ser adotada.  
***Observação:*** Diferentemente do SCAN nesta modalidade não é necessário modificar a Serie de emissão da NF-e

**EPEC**

Havendo indisponibilidade do ambiente da SEFAZ o contribuinte poderá solicitar autorização da NF-e através desta modalidade sem a necessita de prévia autorização da SEFAZ ou da utilização formulários de segurança.

**Passos para utilização:**  
1 – [Alterar a modalidade de emissão](http://tdn.totvs.com/pages/viewpage.action?pageId=422546030)  da NF-e para EPEC;  
2 – Para as NF-e que estão pendentes retorno de autorização da SEFAZ, deverão ser gerados novos movimentos (copias) com novos números para emissão em Contingência;  
3 – Acesse a tela de emissão de NF-e e execute o processo "Enviar NF-e" normalmente;  
4 – Ao consultar a autorização da NF-e, caso a SEFAZ ainda esteja indisponível, o status EPEC/DEPEC ficará como "Autorizado" e o Staus da NF-e ficará como "Pendente" se a SEFAZ já estiver funcionando normalmente os dois status ficaram como "Autorizado";  
5 – Imprima o relatório DANFE clicando no botão "Imprimir DANFE.NET" que ficará disponível na tela de resultado da execução do processo ou selecionando a nota na grid de notas e executando o processo de imprimir o DANFE "Imprimir DANFE.NET;  
6 – Após a cessação dos problemas na SEFAZ e voltando a normalidade de autorização da NF-e, basta consultar a notas com status pendente para obter a autorização. Deverão ser observados os casos que foram necessários gerar copias dos movimentos para as notas que estavam com status Pendente. As mesmas deverão ser Consultadas e Canceladas ou Inutilizadas conforme cada caso;  
Eventualmente podem ocorrer rejeições das notas, neste caso basta corrigir o problema e reenviar a nota na modalidade normal.

***IMPORTANTE!!!* Para que não seja necessário fazer ficar com notas pendentes e efetuar cópias para enviá-las em contingência deve-se adotar o hábito de executar o processo** **[**Monitor da SEFAZ**](http://tdn.totvs.com/display/LRM/Monitor+SEFAZ)****antes de serem iniciados os envios do período.**
