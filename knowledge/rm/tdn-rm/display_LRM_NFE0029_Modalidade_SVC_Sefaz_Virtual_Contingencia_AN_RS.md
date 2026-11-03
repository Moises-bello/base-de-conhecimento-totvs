---
content_hash: aed3dfcb4911affd73e92421965037b4f5dbd41a8dbde0c6d2f878c764860129
fetched_at: '2026-06-29T00:08:12.548556+00:00'
page_id: '243642946'
product: rm
source: tdn-rm
title: NFE0029_Modalidade_SVC_Sefaz_Virtual_Contingencia_AN_RS
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0029_Modalidade_SVC_Sefaz_Virtual_Contingencia_AN_RS
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 11.52 |
| **Ocorrência:** | Contingencia SVC (Sefaz Virtual de Contingência (AN) ou (RS)) |
| **Passo a passo:** | Introdução:  Esta alternativa de contingência substituiu a alternativa anterior de uso do SCAN (Online - desativado em 30/09/14), com a vantagem de eliminar a necessidade de emissão da NF-e em uma Série específica;  Sefaz Virtual de Contingência – é alternativa de emissão de NF-e em contingência com transmissão da NF-e para uma das Sefaz Virtuais de Contingência. Nesta modalidade de contingência o DANFE pode ser impresso em papel comum e não existe necessidade de transmissão da NF-e para a SEFAZ de origem quando cessarem os problemas técnicos que impediam a transmissão.  **IMPORTANTE:** A utilização da SVC depende de ativação da SEFAZ de origem, o que significa dizer que a SVC só entra em operação quando a SEFAZ de origem estiver com problemas técnicos que impossibilitam a recepção da NF-e.  **Não há necessidade de alteração da seria para 900 a 999.**  1 - Alterar o a modalidade de operação para contingência SVC em: Vendas | Faturamento | SPED NF-e (Estadual) | Processos | Alterar Modalidade | selecione entre:  SVC - AN Quando os estados forem: AC, AL, AP, DF, ES, MG, PB, RJ, RN, RO, RR, RS, SC, SE, SP, TO;  SVC - RS Quando os estados forem: AM, BA, CE, GO, MA, MS, MT, PA, PE, PI, PR;    2 - Envie, consulte e imprima a NF-e normalmente.  3 - Após a SEFAZ voltar ao normal, volte a modalidade de operação para normal em: Vendas | Faturamento | SPED NF-e (Estadual) | Processos | Alterar Modalidade | normal;      **Observações:**   Ao alterar a modalidade para “Contingência SVC (AN ou RS)”, devem-se observar os seguintes procedimentos:  1 – Monitorar o status do serviço do SVC para verificar se o serviço está disponível para sua UF e/ou verificar no site da SEFAZ se foi disponibilizado o serviço;  2 – Geração de novo arquivo XML da NF-e com o campo “tp\_emis” alterado para 6 – SVC AN ou 7 – SVC RS. Isto o RM faz automaticamente ao alterar a modalidade de operação;   **Caso o movimento tenha sido enviado anteriormente para a modalidade “NORMAL” e esteja com o status “PENDENTE” é necessário realizar a emissão de um novo movimento para o envio da NF-e na modalidade Contingência SVC.**   **Isto porque o lote que realizou a transmissão desta nota pode ter sido recebido pela SEFAZ, mas o Web Service da SEFAZ não retornou os dados da autorização da nota.**   **Quando o serviço for estabelecido, a nota que se encontrava com o status Pendente no sistema, deverá ser consultada, buscando assim os dados de autorização da mesma para posteriormente ser cancelada, uma vez que a nota que terá valor fiscal será a nota enviada e aprovada em contingência Online (SVC).**   3 – Transmissão da NF-e para o SVC e obtenção da autorização de uso;(Ao contrário da Contingência Offline, o SVC é enviado à SEFAZ normalmente e consultado a sua autorização);   4 – Impressão do DANFE em papel comum, utilizando o mesmo relatório da modalidade normal;  5 – Após o Web Service da SEFAZ estar disponível novamente, o emissor deve voltar à modalidade de operação para “NORMAL” |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
