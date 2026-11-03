---
article_id: 38225101155607
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: dd379a1e541aeccb7e8601131ecd66a2822fd57d7d72931665124ce90122e7cc
fetched_at: '2026-06-28T22:39:09.807564+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento – Backoffice (Linha Protheus) – SIGAEST – MATA010 – Campo B5_CEME
  continua obrigatório mesmo após tentativa de desativação
type: support-article
updated_at: '2026-02-06T19:20:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38225101155607-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Campo-B5-CEME-continua-obrigat%C3%B3rio-mesmo-ap%C3%B3s-tentativa-de-desativa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38225081752471) Tempo aproximado para leitura: 00**:01:00 min**  
  
**Ocorrência**  
É possível remover a obrigatoriedade de preenchimento do campo **B5\_CEME** (tabela SB5 – Dados complementares do produto) na rotina **MATA010 – Cadastro de Produtos?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**  
A rotina **MATA010 foi reescrita em tecnologia MVC** e passou a permitir a exibição de campos de tabelas relacionadas por meio do parâmetro **MV\_CADPROD**.

Nesse novo comportamento:

* A validação de obrigatoriedade do **B5\_CEME (SB5)** ocorre **somente quando o usuário interage com os campos da aba/quadro da SB5**.
* Caso não haja interação, a validação não é disparada.
* O mesmo conceito se aplica às demais tabelas complementares, como **SBZ** e **SGI**.

Além disso, o campo possui regra estrutural de obrigatoriedade definida no padrão do sistema, **não sendo possível remover essa obrigatoriedade nativamente via configuração**.

**Solução**  
Não é possível desativar a obrigatoriedade do campo **B5\_CEME** por parametrização padrão.

Como alternativa, caso seja necessário um comportamento diferente, recomenda-se:

* Utilizar **pontos de entrada do MVC** para implementar validações personalizadas
* Criar regras específicas conforme a necessidade do cliente

Documentação de apoio:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=208345968>

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
