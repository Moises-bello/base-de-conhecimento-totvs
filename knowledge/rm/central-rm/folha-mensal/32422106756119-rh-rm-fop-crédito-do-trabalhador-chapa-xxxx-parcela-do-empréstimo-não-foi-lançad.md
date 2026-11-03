---
article_id: 32422106756119
category: Folha Mensal
content_hash: 552ee061b71612d6bd47914e19ee43aa4a7c7e82890ad659feaf145eceaf051b
fetched_at: '2026-06-28T22:46:58.065614+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Crédito do Trabalhador - Chapa XXXX: Parcela do empréstimo
  não foi lançada porque o evento XXXX já existe no envelope'
type: support-article
updated_at: '2025-07-23T14:16:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32422106756119-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Chapa-XXXX-Parcela-do-empr%C3%A9stimo-n%C3%A3o-foi-lan%C3%A7ada-porque-o-evento-XXXX-j%C3%A1-existe-no-envelope
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32422092727959) Tempo aproximado para leitura: **00:02:15min**  
**Ocorrência**

Ao realizar o lançamento do grupo de eventos para lançamento do novo crédito trabalhador, o sistema emite a seguinte mensagem de erro: **Chapa XXXX: Parcela do empréstimo EMPT0000002 não foi lançada porque o evento XXXX já existe no envelope**.

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.277

12.1.2410.229

12.1.2502.145

12.1.2506 e superiores

**Causa**

O erro ocorre pois o evento informado para compor a base de cálculo da remuneração do crédito trabalhador já está presente no envelope de pagamento, lançado por outro meio — como grupo de eventos, eventos adicionais ou códigos fixos. Quando o mesmo evento é incluído novamente via parametrizador do crédito trabalhador, o sistema impede o lançamento duplicado para evitar inconsistências.

**Solução**

Para correção, verifique se os eventos utilizados na composição da Base Remuneração Crédito Trabalhador já estão sendo lançados por outro meio, como:

1. Grupo de eventos associado ao envelope (Folha Mensal | Lançamentos | Grupos de Eventos | Aba Eventos do grupo);
2. Eventos adicionais;
3. Códigos fixos cadastrados para o colaborador;
4. Eventos programados.

Caso os eventos já estejam presentes por um desses meios, **remova-os** dessas origens e mantenha-os apenas em **Configurações | Parametrizador | Folha Normal | Eventos Crédito Trabalhador** ou nos anexos do funcionário, pois esses são os locais corretos para essa finalidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32422106741399)

**Observação:** Para verificar quais eventos devem ser informados nessa aba e qual o comportamento do sistema ao informá-los, verifique a documentação: [RH - RM - FOP - Crédito do Trabalhador - Eventos informados no parametrizador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32422821948183-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Eventos-informados-no-parametrizador)

**Saiba Mais:**

* [RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
