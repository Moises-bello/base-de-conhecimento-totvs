---
article_id: 360050318713
category: RH - Integração de Titulo
content_hash: 6e9747c1cfe61d2b4577c681d2363741517960c5d976e83b4d08d0ddb35030f1
fetched_at: '2026-06-28T22:43:36.264120+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como impedir a geração de títulos repetidos no
  GPE
type: support-article
updated_at: '2025-07-15T20:33:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050318713-RH-Linha-Protheus-GPE-Como-impedir-a-gera%C3%A7%C3%A3o-de-t%C3%ADtulos-repetidos-no-GPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33489893755927)Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Como impedir a geração de títulos repetidos no GPE?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**A **geração de títulos** automática pode ser configurada para impedir que os títulos sejam gerados repetidamente através do parâmetro MV\_CONDUPL configurado **MV\_CONDUPL=.T.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074445074)  
  
**A validação das chaves ocorre através dos campos:** Filial - Agrupamento - Prefixo do título - Tipo - Competência - Valor.

Exemplo:   
Manutenção de títulos:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075645653)  
  
Geração de títulos para pensão alimentícia através da rotina GPEM650:   
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075645673)  
  
Após o processo de geração, o PROTHEUS já identifica  de acordo com as chaves citadas acima, que os títulos já existem e  apresenta um log com os títulos que não foram gerados por já se encontrarem no banco de dados:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074445134)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075645693)

**IMPORTANTE:**  
Mesmo que os títulos estejam integrados ao módulo Financeiro, o sistema deverá realizar a validação considerando as seguintes chaves :  
**"Filial", "Agrupamento", "Prefixo do Título", "Tipo do título", "Competência" "Valor"** **e Data Vencimento\***e impedir a geração dos títulos.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Chave de busca de duplicidade de títulos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052211974-RH-Linha-Protheus-GPE-Chave-de-busca-de-duplicidade-de-t%C3%ADtulos)
