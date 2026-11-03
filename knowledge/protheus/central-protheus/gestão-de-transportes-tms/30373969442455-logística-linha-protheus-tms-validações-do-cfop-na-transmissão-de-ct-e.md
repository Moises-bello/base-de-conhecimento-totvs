---
article_id: 30373969442455
category: Gestão de Transportes (TMS)
content_hash: 089cecdbcf98652e820a8c60759a9eab5adcc53d8a3148829b364f1175fc7f94
fetched_at: '2026-06-28T22:45:33.444161+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Validações do CFOP na transmissão de CT-e
type: support-article
updated_at: '2025-03-12T11:37:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30373969442455-Log%C3%ADstica-Linha-Protheus-TMS-Valida%C3%A7%C3%B5es-do-CFOP-na-transmiss%C3%A3o-de-CT-e
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30373924156055) Tempo aproximado para leitura: **00:03:30 min** **Dúvida**Como avaliar as rejeições relacionadas ao **CFOP** na transmissão do **CT-e** ?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
**Solução**As validações e rejeições de **CFOP** seguem as regras definidas no Manual de Orientação do Contribuinte, Leiaute e Regras de Validação do **CT-e** da **SEFAZ**. A seguir, apresentamos as possíveis causas e soluções para esses casos:

* **676 - CFOP informado inválido**
  + Validar se o **CFOP** informado pertence a operação de transporte. Verificar a relação de **CFOP** válidos no **item 12** do **MOC Visão Geral.**
* **519 - CFOP inválido para operação**
  + Verificar o **CFOP** informado considerando a seguinte matriz:
    - Se **UF** de início da prestação for igual a **UF** de fim de prestação (e **UF** fim diferente de **EX**), então o **CFOP** deve iniciar por 5;
    - Se **UF** de início da prestação for diferente de **UF** de fim da prestação (e **UF** fim diferente de **EX**), então, o **CFOP** deve iniciar por 6;
    - Se **UF** fim de prestação for igual a **EX**, então, o **CFOP** deve iniciar por 7.
  + No **Protheus TMS**, para atender a conversão do digito inicial do **CFOP** com base no início e fim de prestação de serviço de transporte, o Sistema converte automaticamente o digito do **CFOP** no momento do cálculo do frete conforme as regiões de origem e destino. Caso tenha esta rejeição e tenha validado que as regiões de início e fim da prestação do documento estão corretas e devidamente cadastradas, sugerimos que **abra um ticket para o time de Atendimento** realizar a análise do seu caso.
* **524 - CFOP inválido, informar 5932 ou 6932**
  + Se **UF** do emitente **for diferente** da **UF** de início da prestação e **UF** de início e fim da  
    prestação forem diferentes de **EX,** então, o **CFOP** deve ser igual a **5932** ou **6932**.   
    **Exceção:** regra não será aplicada na hipótese de Regime Especial da **NFF.**
  + No **Protheus TMS**, para ajustar o **CFOP** utilizado no **CT-e**, identifique a **TES** utilizada no cálculo e ajuste o CFOP no cadastro de **Tipos de Entrada e Saída - MATA080.**
* **908 - CFOP inválido, não informar 5932 ou 6932**
  + Se **UF** do emitente **for igual** a **UF** de início da prestação e **UF** de início e fim da  
    prestação forem diferentes de **EX,** então, o **CFOP** não pode ser **5932** ou **6932**.   
    **Exceção:** regra não será aplicada na hipótese de Regime Especial da **NFF.**
* No **Protheus TMS**, para ajustar o **CFOP** utilizado no **CT-e**, identifique a **TES** utilizada no cálculo do frete e ajuste o **CFOP** no cadastro de **Tipos de Entrada e Saída - MATA080,** posteriormente, estorne o **CT-e** e calcule o frete novamente.

**Importante**  
Nos casos em que o documento seja calculado com uma **TES** indevida, e por consequência utilizando o **CFOP** incorreto, sugerimos revisar suas **Regras de Tributação - TMSA410.  
  
Saiba mais**[Documentos e Manuais CTE SEFAZ](https://dfe-portal.svrs.rs.gov.br/Cte/Documentos)[Configuração de Documentos (TMSA150 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=539703192)  
[Regras de Tributação (TMSA410 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=542150880)   
[Regras por Clientes (TMSA600 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=542151212)

**Glossário  
CFOP** - Código Fiscal de Operações e de Prestações **CT-e** - Conhecimento de Transporte eletrônico  
**MOC** - Manual de Orientações ao Contribuinte **NFF** - Nota Fiscal Fácil  
**SEFAZ** - Secretaria da Fazenda **UF** - Unidade Federativa
