---
content_hash: 961ae8bfb5725d5bc7325dd8b4e2a6ac70f3fb6fa0e323bfa5db21b010cdb3a3
fetched_at: '2026-06-29T00:09:21.181150+00:00'
page_id: '422545853'
product: rm
source: tdn-rm
title: Emissão em Contingência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545853
version: 2
---

O  Sistema  da NFC-e é baseado no conceito de documento fiscal eletrônico: um arquivo eletrônico com as informações fiscais da operação comercial que tenha a assinatura digital do emissor.   
A validade de uma NFC-e está condicionada à existência da respectiva autorização de uso concedida pela Secretaria de Fazenda de localização do emissor ou pelo órgão por  ela designado para autorizar a NFC-e em seu nome.  
A obtenção da autorização de uso da NFC-e é um processo que envolve diversos recursos de infraestrutura, hardware e software. O mau funcionamento ou a indisponibilidade de qualquer um destes recursos pode prejudicar o processo de autorização da NFC-e, com reflexos nos  negócios do emissor da NFC-e que fica impossibilitado de obter a prévia autorização de uso da NFC-e exigida na legislação para a emissão do DANFE para acompanhar a circulação da mercadoria.   
 É aconselhável que os relatórios do DANFE estejam sempre atualizados. Os relatórios podem ser baixados na [página de downloads](https://totvs.fluigidentity.com/cloudpass/?forward=/SPInitPost/receiveSSORequest/zf0y84vo717g8hjx/y6k661wf5a5vh9u11405012401405) do suporte.  
 Atualmente existem as seguintes modalidades de emissão de NFC-e: Normal, Contingência OffLine FS e Contingência OffLine FS-DA. Abaixo serão descritas as modalidades que são para utilização em contingência e os detalhes para emissão das notas nas mesmas.

**FS e FS-DA**

Sendo identificada a existência de qualquer incidente que prejudique ou impossibilite a transmissão das NFC-e e/ou obtenção da autorização de uso da SEFAZ, a empresa poderá adotar as Contingência FS ou FS-DA sendo que para utilizar a contingência FS o DANFE deverá ser impresso com formulário de segurança.

***Passos para utilização:***

1 – Alterar a modalidade de emissão da NFC-e para "Contingência Off-line" (FS) ou "Contingência Off-line FS-DA" (FS-DA);  
2 – Acesse a tela de emissão e selecione a opção Enviar, preencha os parâmetros necessários Filial, Tipo de Movimento, Data Inicial e Final e a numeração;  
3 – Imprima o relatório DANFE NFC-e clicando no botão "Imprimir DANFE.NET" que ficará disponível na tela de resultado da execução do processo ou selecionando a nota na grid de notas e executando o processo de imprimir o DANFE "Imprimir DANFE.NET (RM Reports)";  
4 – Transmitir as NFC-e imediatamente após a cessação dos problemas técnicos que impediam a transmissão da NFC-e, observando o prazo limite de transmissão na legislação. Nos casos que foram necessários gerar copias dos movimentos porque as notas estavam com status Pendente as mesmas deverão ser Consultadas e Canceladas ou Inutilizadas conforme cada caso;

***Observações:***

1 – O relatório DANFE será impressos a partir das informações constantes no XML da NFC-e. Caso após a geração da NFC-e em contingência e impressão do relatório seja identificada alguma necessidade de correção, basta corrigir a informação no campo de origem (Cadastros, movimento, etc.), em seguida executar novamente o processo para geração da NFC-e em contingência para que o XML da mesma seja atualizado e imprimir o DANFE novamente;  
 2 – Ao executar o processo para gerar DANFE em contingência, não serão selecionados Movimentos Cancelados ou movimentos que já estejam com status Pendente, Cancelamento Pendente, Inutilizada, Autorizada, Cancelada ou Denegada para geração da DANFE em Contingência;   
 3 – Observe se as regras fiscais de contingências definidas no manual da SEFAZ foram respeitadas no DANFE e no XMl da nota.
