---
article_id: 360020133472
category: ADVPL - Classe e Função
content_hash: ae3083990b75f4c0742829cd05892aa049d71b038a5c48f5006fbd668971322b
fetched_at: '2026-06-28T22:40:19.498662+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - FWFileWriter como
  gravar no arquivo
type: support-article
updated_at: '2022-01-10T22:30:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020133472-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-FWFileWriter-como-gravar-no-arquivo
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Na documentação para utilizar a nova função de escrita em arquivos:   
<http://tdn.totvs.com/display/framework/FWFileWriter> , não consegui visualizar em momento que grava um texto no arquivo.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Neste utiliza-se o método Write segue exemplo:

```
#Include 'Protheus.ch'  
  
User Function Exemplo()  
Local oFile := c():new("ExFWFileWriter.txt")  
  
//--------------- Se o arquivo já existe, apaga -------------------  
If oFile:Exists()  
 oFile:Erase()  
 EndIf  
   
 //-------------- Cria o arquivo --------------  
 If (oFile:Create())  
 //-------------- Se criou com sucesso, escreve ------------------------------  
 oFile:Write("Teste de escrita!")  
   
 //-------------- Fecha o arquivo -----------  
 oFile:Close()  
 Endif  
   
Return
```
