---
article_id: 1500001312741
category: RH - Relatórios Folha
content_hash: e8e8fde7dd0af0a01df924d4148f0fa7dca5aa3065bae0c945ea7d3b373d0ea7
fetched_at: '2026-06-28T22:43:17.623916+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema apresenta várias páginas com totais por
  Centro de Custo no Relatório da Folha de Pagamento
type: support-article
updated_at: '2025-08-04T14:40:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001312741-RH-Linha-Protheus-GPE-Sistema-apresenta-v%C3%A1rias-p%C3%A1ginas-com-totais-por-Centro-de-Custo-no-Relat%C3%B3rio-da-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25841650636311) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**No Módulo de Gestão de Pessoal, quando solicitamos a impressão de **totais** por **Centro de Custo,** Sistema apresenta **mais de uma página** para o **mesmo Centro de Custo** indevidamente.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Para que o Sistema realize a impressão devida dos **totais** por **Centro de Custo,** é necessário que a pergunta **Impr.Niveis C.Custo** esteja como **Sim.**  
Com esta opção **ativada,** o Sistema traz **separadamente** os totais de cada nível, caso haja uma classificação.  
Quando ela existe, é possível definir o **numero de dígitos** que será apresentado para **cada nível** no momento da impressão do relatório através do parâmetros **MV\_MASCCUS**, por isso é apresentada mais de uma vez.  
  
**Solução**Para que o Sistema apresente apenas **uma** folha com os totais por centro de custo na **impressão** do relatório da folha **(GPER040),** siga os seguintes passos:  
1. Acesse o ambiente **SIGACFG** (Configurador) com usuário que tenha permissão de **administrador;**  
2. Busque no menu a opção Parâmetros em **Ambiente > Cadastros > Parâmetros**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102392413)  
3. Clique em **expandir, busque** pelo parâmetro **MV\_MASCCUS** e depois clique em **editar;**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100217794)

4. **Altere** o conteúdo do parâmetro para que fique em **branco** e clique em **salvar.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102392233)  
  
**Saiba mais:**

[RH - Linha Protheus - GPE - Relatório da Folha de Pagamento Sintético não imprime os Centros de Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000371582-MP-GPE-Relat%C3%B3rio-da-Folha-de-Pagamento-Sint%C3%A9tico-n%C3%A3o-imprime-os-Centros-de-Custos?source=search)

[RH - Linha Protheus - GPE - Parâmetros utilizados para impressão dos relatórios de Folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053937794-MP-GPE-Par%C3%A2metros-utilizados-para-impress%C3%A3o-dos-relat%C3%B3rios-de-Folha?source=search)
