---
article_id: 10920973639575
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: fef1a57ea398b6c389bc36904136d5a5ff227cfe12ee01a2dc9118c543bc8aae
fetched_at: '2026-06-28T22:39:45.341110+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Integração Catálogo
  de Produtos DUIMP
type: support-article
updated_at: '2024-06-19T18:03:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10920973639575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Integra%C3%A7%C3%A3o-Cat%C3%A1logo-de-Produtos-DUIMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17676455308951) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Registrar as informações integradas com o Catálogo de Produtos no Portal Único Siscomex?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*- a partir da versão 12.1.27  
  
**Solução**Esta rotina possibilita registrar as informações integradas com o **Catálogo de Produtos** do Portal Único Siscomex (**DUIMP**).

Permite a inclusão da Integração do **Catálogo de Produtos** para que seja este integrado ao Portal Único do Governo.

1. Clique em **F3** ou lupa e selecione o Cod. Item Catálogo.
   1. Perceba que os campos foram "**gatilhados**" conforme cadastrados no **Catálogo de Produtos**.
   2. O campo "**Versão**" é preenchido de acordo com alguns critérios:
      1. A Numeração da Versão é realizada pelo sistema e, no caso em que a Versão do Catálogo esteja em branco e não haja ainda nenhum registro de integração para o Catálogo, o Sistema inicializará o campo Versão conforme o tamanho do campo, será "**000001**"
      2. Caso haja Registro de Integração já gravado e com Status "**Não** **Integrado**", será mantida a numeração Atual da Versão e excluído o registro da Versão Anterior.
      3. Caso haja versão Atual preenchida para o Catálogo de Produtos, exemplo "**000002**", será preenchida na Integração a próxima numeração que será "**000003**"
      4. Caso haja Versão com Status "**Integrado**", ao incluir nova versão, a anterior será cancelada e a versão incluída ficará com Status "**Não Integrado**".
   3. Os campos não são editáveis, nem as linhas de produtos e/ou Fabricantes, nem as linhas de Atributos são possíveis de excluir.
   4. O campo “**Status Integ**.” é inicializado com o status “**1-Não integrado**”.
   5. O grid com as informações dos produtos é preenchido automaticamente de acordo com as informações já existentes no **Catálogo de Produtos**.
   6. O grid com as informações dos fabricantes é preenchido automaticamente de acordo com as informações já existentes no **Catálogo de Produtos**.
   7. Status possíveis do campo "**Vincular**":
   8. O grid com as informações dos atributos é preenchido automaticamente de acordo com as informações já existentes no Catálogo de Produtos.
2. Confirme a gravação

**Exemplo do procedimento**

**Saiba mais**  
[Integração Catálogo de Produtos](https://tdn.totvs.com/pages/viewpage.action?pageId=547226488)   
[Procedimento para Implantação DUIMP](https://tdn.totvs.com/pages/viewpage.action?pageId=657762135)   
[Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Catálogo-de-Produtos-para-tratativa-da-DUIMP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8423200910487)   
[EIC 001 - FAQ - Novo processo de Importação - Portal Único](https://tdn.totvs.com/pages/releaseview.action?pageId=788602791)
