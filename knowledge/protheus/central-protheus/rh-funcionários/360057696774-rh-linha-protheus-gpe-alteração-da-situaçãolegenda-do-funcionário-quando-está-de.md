---
article_id: 360057696774
category: RH - Funcionários
content_hash: f0fa2085037f6347fbdfe9fd1360183a6cd276e8e5e8d150ccebd02d0c15bf22
fetched_at: '2026-06-28T22:43:27.327227+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Alteração da Situação/Legenda do Funcionário quando
  está de Férias ou Afastado
type: support-article
updated_at: '2026-05-29T19:43:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057696774-RH-Linha-Protheus-GPE-Altera%C3%A7%C3%A3o-da-Situa%C3%A7%C3%A3o-Legenda-do-Funcion%C3%A1rio-quando-est%C3%A1-de-F%C3%A9rias-ou-Afastado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24385941979799) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como funciona a alteração de Situação/Legenda do Funcionário quando está de Férias ou Afastado?  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100125973)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
O sistema valida os lançamentos de Ausências em **Atualizações > Lançamentos > Ausências** para atualização da situação do Funcionário.

**Funcionamento para as ausências padrões do sistema:**  
  
Quando o Afastamento **não for por motivo de Férias**, o sistema altera o *status* para amarelo **somente** quando a quantidade de dias forem **superiores a 15 no mês.**  
Tanto para Férias quando para outros tipos de Afastamento, a alteração é feita com **referência à competência em que o Funcionário estará ausente.**  
  
**Exemplos de funcionamento para as ausências padrões do sistema:**  
  
- **Férias:** Funcionário estará de Férias no período de 11/10/2024 à 09/11/2024, portanto, nos meses de Outubro e Novembro ele terá a legenda **azul**, que representa Férias.  
**- Afastamento:** Funcionário estará ausente no período de 13/12/2024 até 20/01/2025, portanto, nos meses de Dezembro e Janeiro ele terá a legenda **amarela**, que representa Afastamento.  
  
O *status* do Funcionário voltará a ficar **verde** (ativo), **somente após o fechamento do período que contempla a data fim do afastamento**, tanto para Férias quanto para Afastamentos por outros motivos.

Para **tipo de ausências criadas e/ou alteradas pelo usuário**, consulte o [Boletim Técnico](https://tdn.totvs.com/pages/viewpage.action?pageId=312175003) com as definições do cadastro de Tipos de Ausências.

**Saiba Mais**  
[Boletim Técnico - Lançamentos e Tipos de Ausência](https://tdn.totvs.com/pages/viewpage.action?pageId=312175003)  
[RH - Linha Protheus - GPE - Sistema não altera legenda do Funcionário após cálculo da Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016520212-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-altera-legenda-do-funcion%C3%A1rio-ap%C3%B3s-c%C3%A1lculo-da-rescis%C3%A3o)
