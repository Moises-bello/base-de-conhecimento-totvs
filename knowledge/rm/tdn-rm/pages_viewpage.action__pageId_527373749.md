---
content_hash: 82bbcde57f91ce0e1b1bf63b291c56789cf45e2f8d2fbbfc8c03022286a7a432
fetched_at: '2026-06-29T00:10:32.545894+00:00'
page_id: '527373749'
product: rm
source: tdn-rm
title: RMFIS00002_REINF R-1070 – Tabela de Processos Administrativos/Judiciais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527373749
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.27 |
| **Ocorrência:** | Evento R-1070 – Tabela de Processos Administrativos/Judiciais |
| **Ambiente:** |  |
| **Passo a passo:** | Neste evento devem ser informados os Processos Judiciais e Administrativos que influenciam na apuração dos tributos **e somente aqueles que possuem decisão favorável ao contribuinte**, tanto aqueles de autoria do próprio declarando como o de terceiros que afetem a retenção do tributo.  Quando o processo ainda não estiver transitado em julgamento, o valor do imposto deve ser informado como devido e o valor discutido como suspenso. Durante o andamento do trâmite, o evento deve ser alterado informando o fim da validade da informação anterior e informando o início da validade da nova informação.   121º Passo1º Passo **Cadastro de Processo Judicial:** Menu Cadastros | Mais | Processo Judicial e Administrativo.   Imagem  32º Passo2º Passo O sistema permite a geração do Evento R-1070 com Processo Judicial vinculado ao lançamento fiscal ou apenas existente no cadastro, mesmo sem vínculo com lançamentos.   Imagem    43º Passo3º Passo É necessário incluir o evento R-1070 e vincular o evento ao cadastro de Processo Judicial conforme imagem:   Imagem  54º Passo4º Passo Após a inclusão do evento, acessar o menu Processos | Transmitir Evento   Imagem |
| **Observações:** | O processo judicial deve possuir o tributo discutido em seu anexo como pré-requisito da transmissão do evento. |
