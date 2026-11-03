---
article_id: 360027261071
category: Gestão de Transportes (TMS)
content_hash: b9b18f24604141e544ec539a6bd550101af6c633dca90d8557dcea3225dcaba6
fetched_at: '2026-06-28T22:45:27.701980+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Emissão de CT-e Complementar de Imposto
type: support-article
updated_at: '2025-01-23T20:54:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027261071-Log%C3%ADstica-Linha-Protheus-TMS-Emiss%C3%A3o-de-CT-e-Complementar-de-Imposto
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28740759084695)***Tempo aproximado para leitura: **00:03:40 min****Dúvida**Como emitir **CT-e Complementar** de imposto?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**A emissão de um CTe complementar de imposto é necessária quando há necessidade de adicionar valores relativos aos impostos calculados em um **CT-e - Conhecimento de Transporte Eletrônico** já emitido.  
  
**Cadastros necessários:**

* **Configuração de Documentos**Acessar a rotina **TMSA150 - Configuração de Documentos** localizada em:  
  **Atualizações** > **Doctos e Regras** > **Config. Documentos**.  
  Realizar o cadastro para o documento do tipo **CTRC COMPLEMENTO - 8**.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026767412)

Caso deseje utilizar uma série diferente da utilizada no **CT-e** original, não esquecer de ajustar o parâmetro **MV\_ESPECIE**, conforme exemplo:

![Capturar2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026780311)

* **Regras por Cliente:**Acessar a rotina **TMSA600 - Regras por Cliente** localizada em:  
  **Atualizações** > **Doctos e Regras** > **Regras por Cliente**.  
  Realizar um cadastro contendo uma regra para o cliente, ou definir a informação para o cliente genérico para o documento do tipo **CT-e** **de Complemento**.

![Capturar3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026781191)

* **Parâmetro:**  
  Acessar o modulo **SIGACFG - Configurador**localizado em:  
  **Base de Dados**> **Dicionário** >**Base de Dados.**Clicar em **Parâmetros**e buscar o parâmetro **MV\_COMPIMP - Código do componente de frete que será utilizado para complemento de imposto.**

![Capturar4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026782311)

* **Manutenção de Documentos:**Acessar a rotina **TMSA500 - Manutenção de Documentos** localizado em:  
  **Atualizações** > **Transporte** > **Manutenção Docto**s.  
  Selecionar o **CT-e original** > **outras ações** > **Compl. Imposto** > **outras ações** > **Compl. Imposto**. Informe o valor.

![Capturar5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026774012)

Realizar a transmissão do **CT-e Complementar** pelo **Monitor de Transmissão** - **TMSAE70**.  
A alíquota de imposto não é digitada durante o processo, apenas o valor do Imposto complementar.  
Os valores apresentados para o documento na Consulta de documentos - Valor, Imposto e Valor + Imposto, são iguais.  
  
Nos **Livros fiscais** o documento não possuirá base para o imposto, teremos apenas o valor tributado e a alíquota cheia referente a operação do estado.  
No **XML - *Extensible Markup Language*** gerado para este complementar de imposto, vamos supor que o valor complementado no **ICMS** foi de 149,00. Neste caso as *tags* são gravadas da seguinte forma:

![image__5_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403410946839)

O conteúdo da *tag* <**pICMS>** referente a alíquota é de 100%, pois o **SEFAZ** valida se a alíquota de imposto e valor do imposto estão de acordo.  
  
Se apresentarmos no **XML** a Base para imposto do documento original, ou a alíquota de imposto do Estado, o cálculo da alíquota multiplicado pela base do imposto não resultará no valor de imposto complementado. Desta forma, o **SEFAZ**, ao validar as informações recebidas, identificará que o valor do imposto não confere com o cálculo da base x alíquota e então, rejeita o **XML** apresentando a **rejeição 675 - Valor do imposto não corresponde à base de cálculo X alíquota.**No Protheus TMS, a geração do **XML** e impressão do **DACTE** estão disponíveis em fontes abertos aos clientes, logo, eles podem ser adequados para a forma que cada cliente deseja. Caso o cliente deseje informar outra alíquota na *tag* **<pICMS>**, basta adequar o **CTESEFAZ3**, e, ao obter a rejeição do **SEFAZ**, então, o cliente deve abrir uma consulta protocolada no **SEFAZ** questionando a **rejeição 675** ao enviar outra alíquota *tag* **<pICMS>**.

**Saiba mais**  
[Logística - Linha Protheus - TMS - RDMAKES para o CTe e MDFe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24339487959703-Log%C3%ADstica-Linha-Protheus-TMS-RDMAKES-para-o-CTe-e-MDFe)
