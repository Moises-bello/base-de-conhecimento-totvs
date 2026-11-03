---
article_id: 40413578778647
category: eSocial - Eventos Totalizadores
content_hash: e8237fead9248e46c1bf2e40b0c5ba353567e5702371807b145564273b8e3f04
fetched_at: '2026-06-28T22:47:06.922625+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: RH - RM - FOP- eSocial - Nota Orientativa S-1.3 Nº 09/2026 - SESI e SENAI
type: support-article
updated_at: '2026-05-12T17:45:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40413578778647-RH-RM-FOP-eSocial-Nota-Orientativa-S-1-3-N%C2%BA-09-2026-SESI-e-SENAI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40413558479511) **Tempo aproximado para leitura: 00:03:00 min**  
  
**Dúvida**  
O que fazer para atender às orientações da Nota Orientativa S-1.3 Nº 09/2026 do eSocial, referente às contribuições do SESI e SENAI?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**  
Em Abril de 2026 foi publicada a **Nota Orientativa S-1.3 nº 09/2026**, que traz orientações sobre os ajustes necessários no eSocial para empresas contribuintes do Serviço Social da Indústria (**SESI**) e do Serviço Nacional de Aprendizagem Industrial (**SENAI**) que mantinham convênios para arrecadação direta dessas contribuições.

Com a mudança, esses valores passarão a ser apurados por meio do eSocial e recolhidos via DARF, em conjunto com os demais tributos federais, por meio da DCTFWeb. Para isso, será necessário que **as empresas realizem ajustes na Tabela de Lotação Tributária (S-1020)**, incluindo a criação de nova vigência a partir de maio de 2026, com a devida atualização do **FPAS** e do **código de terceiros**, de forma a permitir a correta apuração das contribuições.

A Nota também esclarece que a contribuição adicional devida ao SENAI pelas empresas com **mais de 500 empregados** passará a ser **apurada automaticamente** pelo eSocial, **sem necessidade de ações por parte dos contribuintes.** O sistema considerará o total de empregados vinculados **(categoria 1XX)** às lotações com **FPAS 507 ou 833**, levando em conta toda a empresa, e realizará a geração da contribuição quando esse limite for ultrapassado.

Segue trecho importante da NO junto com as devidas orientações no sistema:

***Recolhimento da contribuição regular devida ao SESI e SENAI***  
*Para que o eSocial possa gerar as contribuições corretamente, as empresas impactadas devem **atualizar as suas Tabelas de Lotação Tributária (S-1020)** com o **FPAS** relacionado à indústria [507] ou à agroindústria [833], **alterando o código de terceiros** {codTercs} de [0067], [0071] ou [0075] exclusivamente para [0079]. A atualização deve ser realizada mediante a criação de **nova vigência nas tabelas**, com início de validade 05/2026.*

O código de terceiros pode ser alterado através do menu **Administração de Pessoal | Seção**, editando a seção, aba **Dados p/ INSS**, campo **Cód. Terceiros (INSS)**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40413578761495)

Caso o parâmetro **Utiliza tomadores de serviço** estiver marcado no parametrizador da Folha de Pagamento, verifique no menu **eSocial | Lotação Tributária** se o parâmetro **Considera Dados da Seção** está marcado. Caso esteja desmarcado, será necessário preencher os campos de **FPAS** e **Código de Terceiros** para correta geração do XML:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40413558481047)

Após alteração dos dados, será gerado um gatilho do S-1020 na fila de eventos do eSocial. Verifique a tag ***iniValid*** e, se necessário, ajuste o campo **Competência** com o mês e ano **05/2026** para gerar corretamente a informação de início de validade no XML.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40413578764439)

**Importante**  
Não há novas implementações a serem realizadas por parte do produto, apenas configurações vinculadas ao Código de Terceiros. A implementação dessas mudanças terá início no **período de apuração de maio de 2026**, ou seja, irá refletir na folha enviada em junho de 2026.  
  
**Saiba mais**  
Para mais informações, acesse:

* [NOTA ORIENTATIVA S-1.3. 2026.09](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-s-1-3-09-2026.pdf)
* [Histórico de Percentuais para INSS no cadastro de Seção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8681885111063)
* [Middleware: Relatório de Conferência de INSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407770756247)
