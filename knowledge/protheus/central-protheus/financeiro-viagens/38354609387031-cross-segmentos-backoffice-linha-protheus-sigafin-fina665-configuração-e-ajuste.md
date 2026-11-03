---
article_id: 38354609387031
category: Financeiro - Viagens
content_hash: 3af184ea1df53c4130977a37a5616fe496d64037655bd34eecda159ecaf72707
fetched_at: '2026-06-28T22:38:21.251069+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA665 - Configuração
  e ajuste de valores de adiantamento em viagens
type: support-article
updated_at: '2026-02-13T11:35:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38354609387031-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA665-Configura%C3%A7%C3%A3o-e-ajuste-de-valores-de-adiantamento-em-viagens
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38354609365015) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como realizar o ajuste manual do valor de adiantamento em solicitações de viagens e quais as limitações de configuração via Wizard na rotina FINA691?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
No processo de viagens do Protheus, a flexibilidade no valor do adiantamento depende da configuração inicial no Wizard (FINA691).

1. **Limitação do Wizard (FINA691):** Quando um valor é definido no campo "Valor Fixo" dentro do Wizard de Configuração, este valor será replicado para todas as solicitações, impedindo a edição manual do montante no momento da solicitação de viagem **FINA666**.
2. **Ajuste de Valor (FINA665):** Para permitir que o solicitante insira qualquer valor de adiantamento, a configuração de "Valor Fixo" no Wizard deve ser mantida zerada/vazia. O ajuste e a inserção do valor desejado deverão ser realizados através da rotina de viagens **FINA665**.
3. **Rotina FINA666:** Para esta rotina, o sistema mantém a premissa de valor fixo para adiantamentos, permitindo adicionalmente a configuração de limites de quantidade de adiantamentos por dia.

**Exemplo tela do Wizard da rotina FINA691:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38354692202263)

---

### **Passos**

1. Acesse a rotina **FINA691** (Wizard de Configuração).
2. Avance até a etapa de **Adiantamento**.
3. Para permitir valores variáveis na solicitação, certifique-se de que os campos de **Valor Fixo** e **Adiantamento sem Pernoite** estejam zerados.
4. Finalize o Wizard para salvar as alterações.
5. Acesse a rotina **FINA665** para prosseguir com a solicitação e informar o valor de adiantamento manualmente conforme a necessidade.
6. Após a aprovação da solicitação e do adiantamento, o sistema gerará automaticamente o título no **Contas a Pagar (FINA050)** com o prefixo configurado (ex: ADP).

**Saiba mais:** [**Viagens - Financeiro**](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)
