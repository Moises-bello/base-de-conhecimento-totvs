---
content_hash: 8a3fe21bb6de72f969cd883bc1ccc6df23800702d8d864c2738a715745ed8bc4
fetched_at: '2026-06-29T00:08:34.879811+00:00'
page_id: '274850042'
product: rm
source: tdn-rm
title: NFCE0005_NFC-e_Envio_de_NFC-e.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274850042
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NFC-e - Nota Fiscal do Consumidor Eletrônica |
| **Versões:** | A partir da 12.1.7 |
| **Ocorrência:** | Envio de NFC-e |
| **Passo a passo:** | **Introdução:**  Este documento tem como objetivo orientar o envio do movimento de NFC-e. Esclarecendo o processo de entrada em contingencia automaticamente.  Diferente da NF-e, que deve ser enviada e em seguida consultada, o processo de NFC-e é síncrono, ou seja, a SEFAZ já retorna a autorização/rejeição no momento do envio. Logo, ao enviar a NFS-e, o registro será autorizado ou rejeitado. Não existindo o status de pendente para NFC-e.    Selecione o movimento, vá em: Processos | Enviar NF-e/NFC-e.      A NFC-e será autorizada ou rejeitada imediatamente, não havendo a necessidade de consultar o registro (como é feito para NF-e).      Por se tratar de um processo sincrono, quando o TSS por algum motivo, não conseguir comunicar com a sefaz (sefaz fora do ar, problemas com internet, bloqueios de rede, proxy, firewall e etc), tanto o TSS quanto o RM Nucleus entraram em modo de contingencia off line e o registro enviado, passará para o status de "Cancelamento Pendente".  Selecione o movimento, vá em: Processos | Enviar NF-e/NFC-e.      Devido a problemas de comunicação entre o TSS e a SEFAZ fora do ar, problemas com internet, bloqueios de rede, proxy, firewall e etc),  tanto o TSS quanto o RM Nucleus entraram em modo de contingencia off line.       O registro enviado, passará para o status de "Cancelamento Pendente".      Quando a situação ocorrer, deve-se realizar uma copia do movimento que esta com status de "Cancelamento pendente".      E envia-lo em contingencia.      Após o envio em contingencia o relatório DANFE estará disponível para impressão.      Relatório DANFE com a informação de que a NFC-e foi gerada em contingencia offline.      Para verificar a disponibilidade da SEFAZ realize o seguinte processo: Vá em processos | "Consultar Monitor Sefaz".  Quando o problema que estava impedindo a comunicação (sefaz fora do ar, problemas com internet, bloqueios de rede, proxy, firewall e etc) entre o TSS e sefaz for sanado.  Para alterar a modalidade de operação, vá em: Processos | Alterar Modalidade de Operação. Selecione o "modelo 65", em seguida altere a modalidade para "Normal".      Selecione os registros com status de "Contingencia" e realize a consulta em: Processos | Consultar autorização.  IMPORTANTE: Diferente do processo de NF-e, os registros com status "CONTINGENCIA" não devem ser enviados após a alteração da modalidade para normal. Os registros devem ser apenas consultados.        Selecione os registros com status de "Cancelamento Pendente" e realize a consulta em: Processos | Consulta de Eventos.        Acesse o Cadastro de filiais| edite a filial | Anexos | NF-e/NFC-e Inutilizadas.      Observe que o registro que estava com status de "Cancelamento Pendente" foi "Inutilizada". |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
