---
article_id: 360052156234
category: RH - Cadastros
content_hash: b632a29dc0854b22901e512c81ae2bd36320b368dca4f2a1c543863007de3dd1
fetched_at: '2026-06-28T22:43:25.914895+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - FWNOWIDTH valor atribuído difere do tamanho do
  campo (Desc.Funçao)
type: support-article
updated_at: '2025-10-31T12:08:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052156234-RH-Linha-Protheus-GPE-FWNOWIDTH-valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Desc-Fun%C3%A7ao
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26938278114583) Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Em **Gestão de Pessoas** ao incluir uma convocação, no **campo função** aparece o erro abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083901474)  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**

O erro ocorre quando os campos **V7\_DFUNC**, **RJ\_DESC** tem tamanho de campo diferente de 20, não sendo permitido  realizar alteração.

Contudo, a informação de descrição de função para eventos do E-Social (S-1030) tem como origem a tabela **C8V** onde o campo C8V\_CODIGO permite até 30 caracteres.

**Solução**

Verifique via **Configurador** o volume dos campos V7\_DFUNC / RJ\_DESC / C8V\_CODIGO se estão de acordo com o padrão.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083902314)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083902374)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083902514)

Consultar a SX3 via APSDU e verificar o volume de campo nas tabelas SV7/SRJ/C8V  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085083133)  
  
Caso algumas desses informações esteja incorreta, deve-se retornar para o volume padrão.  
  
OBS: Se mesmo após as alterações o erro permanecer, verifique se no cadastro de funções possui funções com mais de 20 caracteres cadastradas, se houver será necessário reduzir a nomenclatura para o volume de 20 caracteres.

**Saiba mais:**

[RH - Cadastros](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781894-RH-Cadastros)
