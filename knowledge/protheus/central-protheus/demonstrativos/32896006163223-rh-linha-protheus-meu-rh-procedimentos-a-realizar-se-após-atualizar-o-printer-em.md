---
article_id: 32896006163223
category: DEMONSTRATIVOS
content_hash: 6e360f92dc9bf7fef23219cf93ec46eff0bd713df6ed1056df81bc3d4d67f274
fetched_at: '2026-06-28T22:44:38.343698+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - Meu RH - Procedimentos a realizar se, após atualizar
  o PRINTER em LINUX, downloads em pdf não funcionarem mais
type: support-article
updated_at: '2026-06-19T15:47:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32896006163223-RH-Linha-Protheus-Meu-RH-Procedimentos-a-realizar-se-ap%C3%B3s-atualizar-o-PRINTER-em-LINUX-downloads-em-pdf-n%C3%A3o-funcionarem-mais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32896006145559) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Quais procedimentos realizar se, após a atualização do PRINTER em LINUX, os downloads em .pdf não funcionarem mais?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões   
  
**Solução**  
Quando os *downloads* no Meu RH não estiverem sendo realizados, tendo falhas ou erros, neste caso, **especificamente, tivemos em LINUX**, uma **atualização no** ***PRINTER*****.**  
  
Anteriormente, era necessário em Sistema Operacional LINUX, ter dois arquivos: o *pdfprinter* e o *printer*.  
**Houver uma unificação destes arquivos.**  
  
Por isso, será necessário que em todos os serviços *appserver*, **deletem o** ***pdfprinter*** **e o** ***printer*** que estiverem nas pastas, deixando**somente o** ***printer*** **a partir de 15/04/2025**  
<https://suporte.totvs.com/portal/p/10098/download#000006/368/TFSC/>   
  
**IMPORTANTE:**  
Após essa unificação do *PRINTER*, não teremos mais o *pdfprinter* nas pastas do binário, somente o *printer* para *LINUX*.  
  
Esta versão do *printer* nova tem algumas dependências de LIB do sistema, para validar o funcionamento precisarão junto a equipe de Infra/TI de sua Empresa, executar um **comando ./printer -v,** com isso, se gerar a informação de versão significa que está funcionando, **caso contrário, vai avisar qual dependência de LIB está faltando.**  
  
O comando em questão, executa o programa *printer* localizado no diretório atual, com o parâmetro -v, que depende de como o programa printer foi implementado.   
  
Geralmente executa uma destas duas situações:  
- Exibe a versão do programa.  
- Ativa o modo detalhado (verbose) de execução.  
  
Essas LIBS são as bibliotecas do *Linux*, que são dependências de sistema operacional.  
  
**Dica:**  
**Excluir e reinstalar o libglvnd-opengl,** este trata-se de um componente de *software* relacionado à renderização gráfica no *Linux*, mais especificamente **parte da biblioteca GLVND (GL Vendor-Neutral Dispatch)**, cujo objetivo é permitir a convivência de múltiplos *drivers* OpenGL no mesmo sistema de forma organizada e segura.  
  
**Para cliente em Cloud,** favor abrir um *ticket* para a Equipe correspondente, citando esta documentação e solicitando o apoio na atualização e correção.  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
