---
article_id: 1500006129782
category: Gestão Ambiental (SIGASGA)
content_hash: 7e71972b22267f941078baa7b049871c06f4d5a0150116d1c938523f51c15d2e
fetched_at: '2026-06-28T22:42:38.451821+00:00'
product: protheus
section_id: 360012117893
source: central-protheus
title: Manufatura - Linha Protheus - SGA - Preenchimento do campo Status na rotina
  de Log. de Retirada
type: support-article
updated_at: '2021-08-30T16:42:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006129782-Manufatura-Linha-Protheus-SGA-Preenchimento-do-campo-Status-na-rotina-de-Log-de-Retirada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:01:10 min****Dúvida**Como funciona o preenchimento do campo **Status - TDC\_STATUS** relacionado ao parâmetro **MV\_NGSGASF - Define se na abertura de fichas de movimentação de resíduos o status deve vir igual a 3 - Armazem.**?   
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão Ambiental (SIGASGA) - Versão 12  
  
**Solução**Segue abaixo os passos para entendimento do parâmetro **MV\_NGSGASF**:  
1. Acesse o **Configurador - SIGACFG**2. Em **Ambiente / Cadastro / Parâmetros**, altere o parâmetro **MV\_NGSGASF** para **1 – Sim**.  
3. A rotina **Cadastro de FMR's - SGAA500** não será mais utilizada. E ao acessá-la será apresentada a mensagem: O parâmetro **MV\_NGSGASF** está habilitado, portanto, a inclusão de **FMR** deve ser feita pela rotina de **Logística de Retirada - SGA510**.  
4. Quando acessar a rotina de **Logística de Retirada - SGAA510** o campo **Status - TDC\_STATUS** virá preenchido com o conteúdo **3 – Armazém**, o usuário iniciará o processo pela rotina de **Logística de Retirada - SGAA510.**5. Altere o parâmetro **MV\_NGSGASF = 2 – Não**, a rotina segue o processo atual, o campo **Status - TDC\_STATUS** vem preenchido com **1 – Ponto de Coleta** e a rotina de **Cadastro de FMR's - SGAA500** vem habilitada normalmente.
