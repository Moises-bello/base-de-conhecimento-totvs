---
article_id: 360020733692
category: SIGAACD - Automação e Coleta de Dados
content_hash: 4ef082616f6dae08a9406180fd53ed794250bb57957af6c105f1011cce50ff7e
fetched_at: '2026-06-28T22:39:11.387674+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Após atualização o
  meu ACD não está imprimindo.
type: support-article
updated_at: '2025-12-17T12:20:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020733692-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Ap%C3%B3s-atualiza%C3%A7%C3%A3o-o-meu-ACD-n%C3%A3o-est%C3%A1-imprimindo
---

Após atualização, se o ACD não estiver imprimindo, deve-se recompilar os RDMAKES, reconfigurar o parâmetro MV\_ACDCB0, revisar a configuração do local de impressora e verificar se há registros na tabela CB0 usando a rotina ACDA130. Caso haja registros, o problema pode estar na impressora física.

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24763660016023) Tempo aproximado para leitura: **00:01:00 min***  
  
**Dúvida**  
ACD - Após atualização o meu ACD não está imprimindo. O que devo fazer?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

1. Recompilar os seus **RDMAKES**.
2. Reconfigurar o parâmetro **MV\_ACDCB0** conforme a sua necessidade.
3. Revisar a configuração do seu local de impressora.
4. Consultar se está gerando os registros na tabela de etiquetas (**CB0**), use a rotina Consulta   Geral de Eventos(**ACDA130**). Se estiver gerando registros, terá que revisar a impressora   fisicamente.

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas#:~:text=Saiba%20Mais%3A,Coleta%20de%20Dados)
