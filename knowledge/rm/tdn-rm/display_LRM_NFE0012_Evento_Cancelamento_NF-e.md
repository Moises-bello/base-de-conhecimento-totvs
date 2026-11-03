---
content_hash: d9dd1257412a92790474bfb1b2845297196a7342b97085e9000de8fadb91c44f
fetched_at: '2026-06-29T00:08:10.892819+00:00'
page_id: '241699482'
product: rm
source: tdn-rm
title: NFE0012_Evento_Cancelamento_NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0012_Evento_Cancelamento_NF-e
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Evento - Cancelamento de NF-e por evento |
| **Passo a passo:** | **Introdução:**  A partir do dia 01/12/2012 o método de cancelamento de NF-e foi alterado conforme AJUSTE SINIEF5, DE 30 DE MARÇO DE 2012. O processo de Cancelamento é feito através de Evento como já é feito com a Carta de Correção Eletrônica.  **Gerando o Cancelamento por Evento**     Para gerar o Cancelamento por Evento, acesse o menu: Vendas | Faturamento | SPED NF-e (Estadual), selecione a NF-e a ser cancelada. Vá em | PROCESSOS | ENVIO DE EVENTO NF-e.       Será aberta uma nova visão com o nome “ENVIO DE EVENTO NF-E”, selecione o Tipo de Evento como Cancelamento da NF-e, preencha a solicitação de cancelamento com no minimo 15 dígitos e execute o processo.  **OBSERVAÇÃO:** Ao selecionar cancelamento, o sistema verificará se o movimento possui alguma integração (fiscal, contábil, financeira e etc.) que possa impedir o cancelamento automático do movimento após a NF-e ser cancelada pela sefaz. Desta forma, será apresentado ao usuário  uma mensagem informando a existência da integração e questionando se o usuário deseja proseguir com o processo. Caso exista integração, e o usuário decida continuar com o processo, deve ficar ciente que o registro da NF-e ficará com status de cancelamento pendente até que a integração  seja desfeita. O sistema permite ao usuário a continuar com processo, devido ao prazo de cancelamento da NF-e ser de 24 horas.    Será apresentada a tela de conclusão com a seguinte informação: **“A execução do processo foi concluída com sucesso”**  **OBSERVAÇÃO:** O texto digitado para a correção não pode ter quebras de linha (<<Enter>>).  Após realizar o envio do evento, é necessário realizar a consulta do Cancelamento. Para realizar a consulta acesse o menu | ANEXOS | EVENTOS DA NF-E:    Selecione o evento e clique em | PROCESSOS | CONSULTA EVENTO NF-E: |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
