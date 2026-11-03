---
article_id: 4418641704087
category: Rescisão
content_hash: 3457702ee3777cb3e12d92a3815564774e2e641620155088418ea6ec6b7c6324
fetched_at: '2026-06-28T22:46:54.422030+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Seguro Desemprego: Erro ao calcular campo CampoSDDDD01'
type: support-article
updated_at: '2024-09-16T19:43:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418641704087-RH-RM-FOP-Seguro-Desemprego-Erro-ao-calcular-campo-CampoSDDDD01
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao realizar a geração do Seguro Desemprego apresenta o seguinte erro:   
  
**Erro ao calcular campo CampoSDDDD01 - System.ArgumentOutOfRangeException: O índice e o comprimento devem se referir a um local dentro da cadeia de caracteres.**  
**Nome do parâmetro: length**  
**em System.String.Substring(Int32 startIndex, Int32 length)**  
**em RM.Fop.Dominio.Relatorio.CampoSDDDD01.DoCalcula()**  
**em RM.Fop.Dominio.Relatorio.CampoRelatorioBase.Calcula()**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre, pois há uma divergência entre a máscara do telefone informado no cadastro do funcionário e a máscara para telefone no Parametrizador.    
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse: **Configurações | Parametrizador | RH - Máscaras e Quebras** e verifique os campos **Máscara para telefone** e **Máscara para telefone (sem DDD).**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8907098109079/mceclip0.png)  
  
2. Logo, acesse: **Administração de Pessoal | Funcionários | Edite o cadastro do funcionário | aba Endereço Principal | campo Telefone** e parametrize, conforme número de caracteres da máscara no Parametrizador.  **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8907151388823/mceclip1.png)**
