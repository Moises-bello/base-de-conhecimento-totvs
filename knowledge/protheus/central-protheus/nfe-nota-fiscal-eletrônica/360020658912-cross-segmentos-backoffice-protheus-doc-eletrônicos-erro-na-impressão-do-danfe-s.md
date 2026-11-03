---
article_id: 360020658912
category: NFe - Nota Fiscal Eletrônica
content_hash: 082c8ae630eb7359e6cbaf063876b5f2875a6bb857c07a00f028e99a26d02a18
fetched_at: '2026-06-28T22:40:01.839512+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Erro na impressão
  do DANFE, sistema só cria arquivo .rel e não realize a impressão do DANFE'
type: support-article
updated_at: '2025-12-26T16:44:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020658912--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Erro-na-impress%C3%A3o-do-DANFE-sistema-s%C3%B3-cria-arquivo-rel-e-n%C3%A3o-realize-a-impress%C3%A3o-do-DANFE
---

**Dúvida** Erro na impressão do DANFE, sistema só cria arquivo .rel e não realize a impressão do DANFE

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**Verifique se o caminho que consta no parâmetro **MV\_RELT** existe dentro da pasta **Protheus\_data** e esta com permissão liberada, caso não exista crie uma pasta e insira o caminho no parâmetro, esta pasta deve ser criada dentro da pasta **Protheus\_data**  
  
Verifique também as seguintes situações:  
  
Caso possua espaço no nome da impressora, renomeie o nome sem espaços (ex: minha impressora, alterar para minha\_impressora)  
  
Verificar na estação local se possui o **Printer.exe,** caso não possua, copiar e colar:  
  
WINDOWS 32 BITS:  
  
- Copiar o arquivo **printer.exe** para a pasta **WINDOWS\SYSTEM32**  
- Copiar o arquivo **printer.exe** para o disco local C:/ da maquina que está efetuando a impressão  
  
WINDOWS 64 BITS:  
  
- Copiar o arquivo **printer.exe** para a pasta **WINDOWS\SYSWON64**,  
- Copiar o arquivo **printer.exe** para o disco local C:/ da maquina que está efetuando a impressão  
  
Segue link para atualizar o printer  
  
64 BITS  
<https://suporte.totvs.com/portal/p/10098/download#detail/693168>  
  
32 BITS  
<https://suporte.totvs.com/portal/p/10098/download#detail/693163>
