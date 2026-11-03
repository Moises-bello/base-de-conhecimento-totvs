---
article_id: 360016780631
category: RH - Folha de Pagamento
content_hash: 3eb3d11f17e07fb1bda974511f8f946bb6f7422246e54e2d1aa4d42236fd553c
fetched_at: '2026-06-28T22:44:15.006022+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Impressão de relatórios em formato PDF apresenta
  primeira página em branco
type: support-article
updated_at: '2025-07-23T17:24:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016780631-RH-Linha-Protheus-GPE-Impress%C3%A3o-de-relat%C3%B3rios-em-formato-PDF-apresenta-primeira-p%C3%A1gina-em-branco
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23921646900631)  Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao encaminhar qualquer relatório não personalizado para impressora ou exportá-lo em formato PDF é gerado uma folha em branco no início/ fim do relatório.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O sistema gera essa folha em branco no **início** ou no **fim** do relatório para que todos os arquivos enviados para impressora não se misturem no momento da impressão. Isso pode acontecer quando um usuário encaminha **mais de um arquivo** ou **vários usuários** encaminham arquivos para a mesma impressora.  
  
Caso não queira a impressão dessa folha, é necessário ajustar o conteúdo dos parâmetros **MV\_CANSALT**e **MV\_SALTPAG** no configurador SIGACFG.

**MV\_CANSALT** - Define se permite ou não o envio de uma página em branco após a impressão. Caso afirmativo será considerado o parâmetro MV\_SALTPAG. **Conteúdo**: .T. = Sim; .F. = Não

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23921642311831)

**MV\_SALTPAG** - Indica se o salto de pagina deverá ser dado antes ou depois da impressão do relatório. Saltar pagina no início da impressão? **Conteúdo**: S = Salta no início da impressão; N= Salta depois da impressão

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23921642326807)

**Sabia Mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)

[RH - Relatórios Cadastros/Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843654-RH-Relat%C3%B3rios-Cadastros-Funcion%C3%A1rios)

[RH - Relatórios Previdenciários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011982373-RH-Relat%C3%B3rios-Previdenci%C3%A1rios)
