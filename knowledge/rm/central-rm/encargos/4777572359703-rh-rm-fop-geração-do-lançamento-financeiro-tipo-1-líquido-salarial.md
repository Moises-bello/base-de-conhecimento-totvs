---
article_id: 4777572359703
category: Encargos
content_hash: 9af999c8c12bb3230a6cda694c50e1a61e431608b299d22ef6593668cbbdb377
fetched_at: '2026-06-28T22:46:53.171157+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração do lançamento financeiro tipo 1 - Líquido Salarial
type: support-article
updated_at: '2025-08-01T21:37:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4777572359703-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-lan%C3%A7amento-financeiro-tipo-1-L%C3%ADquido-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24231526861463) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como fazer geração do lançamento financeiro tipo 1 - Liquido Salarial?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para fazer a geração do lançamento financeiro tipo 1-Liquido Salarial, siga as orientações abaixo:  
1. Após o lançamento da folha, cadastrar o parâmetro financeiro em **Encargos | Cadastros Financeiros | Parâmetros**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006126252567)  
  
  
2. Com esse tipo de lançamento financeiro:

\* O sistema irá buscar o líquido salarial dos colaboradores ativos;

\* O campo **Tipo de Documento** é como a informação será levada para o lançamento financeiro;

\* O campo **Cód. Fornecedor** informa o fornecedor que é ligado ao lançamento financeiro;

\* O campo **Fórmula** só será habilitado se o tipo for 7. Mas, nesse caso o tipo é 1. Então, o sistema faz a busca de forma automática;

\* O campo **Período de Cálculo de Rateio** será preenchido como **1 - Mês Atual** ;

\* A flag **Usar histórico padrão** deve estar marcada.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33888906369175)

3. Na aba de Parâmetros , deve-se preencher conforme a necessidade da empresa:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006224886167)  
  
4. Na aba **Lançamentos Ativos** , deve-se marcar **Lançamentos de Folha** ou o lançamento ativo que amarrará este lançamento à rotina:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006210726679)  
  
5. Por fim, clique em **Salvar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33888906370199)**  
  
6. Para gerar o lançamento financeiro, acesse: **Encargos | Geração dos Lançamentos :** **![](https://centraldeatendimento.totvs.com/hc/article_attachments/33888953961239)**7. Deve-se fazer a parametrização do lançamento, selecionando os colaboradores e período:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006303617303)  
  
8. Na próxima tela da geração, selecione o mesmo lançamento ativo utilizado conforme demonstrado no passo 4 e avance.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006288815895)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006306976407)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006398655383)  
  
9. Uma vez gerado com sucesso, será possível consultar o lançamento em: **Encargos | Lançamentos | Lançamentos (Gestão Financeira)**.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006450849431)  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006452236823)  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11006472106263)  
  
**Saiba mais**  
[Cadastros financeiros](https://tdn.totvs.com/display/public/LRM/Cadastros+Financeiros)
