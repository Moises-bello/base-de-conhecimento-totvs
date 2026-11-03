---
content_hash: 5b69b1f7e657fdfb15dad0d3b1c3140e0bda2032ad1bd37e02d8b7337c43a19b
fetched_at: '2026-06-29T00:05:49.878308+00:00'
page_id: '1042910853'
product: rm
source: tdn-rm
title: Reajuste de Valores na Tabela de Preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1042910853
version: 8
---

---

VERSÕES HOMOLOGADAS

* + - **12.1.2506.253** ou superior
    - **12.1.2510.176** ou superior
    - **12.1.2602.1** ou superior

## 📈 **Reajuste de valores**

Este processo permite a atualização massiva e controlada dos valores de crédito baseada em um índice percentual.

O reajuste **não** é global; ele é aplicado cirurgicamente respeitando a combinação de **Filial** e **Período Letivo**. Durante a execução, o sistema exige que seja informado o período letivo de cada filial que possua matriz aplicada vinculada às tabelas selecionadas.

O novo valor terá efeito a partir do período letivo indicado para cada unidade.

Mão na massa: Exemplos práticos 

* Filial 1 - 2025/2
* Filial 2 - 2026/1
* Filial 3 - 20252
* Filial 4 - 2025-2

Neste exemplo, durante o processo é necessário informar o período letivo de cada filial que tenha matriz aplicada vinculada com as tabelas de preço selecionadas. E o reajuste será aplicado **a partir** do período letivo informado:

Ao clicar no processo de reajuste, caso exista alguma tabela de preço, **Inativa** ou com valor de **disciplina** com **preenchimento incompleto**, selecionada um alerta será exibido informando que algumas tabelas de preço não serão listadas para o processo de reajuste:

Na tela de reajuste todos campos são obrigatórios sendo necessário que todos sejam informados para simular o reajuste e efetuar sua confirmação:

Para informar os períodos letivos por filial basta clicar sobre o campo de período letivo, será exibida a listagem de Filiais com a possibilidade de informar o período letivo para cada uma delas:

Com os campos preenchidos corretamente o botão **Simular reajuste** fica disponível:

Simulado o reajuste é possível consultar os valores por tabela de preço, todas tabelas selecionadas ficam disponíveis para conferência antes de salvar o reajuste (opção **Confirmar reajuste**).

Com a simulação executada, o botão **Confirmar reajuste** é habilitado possibilitando a efetivação do reajuste nas tabelas de preço.

Com o processo finalizado uma mensagem informativa de sucesso é exibida. E a coluna Data do último reajuste, na listagem de tabelas de preço é preenchida com a data do reajuste.

#### **⚙️Regras de Reajuste**

**🔒 Segurança e Limites**

* Permissão de acesso específica por perfil.
* Limite de **20 tabelas** por processo.
* Exclusivo para tabelas **Ativas/Preenchidas**.
* Permite apenas **Acréscimo Percentual** nunca como redução.
* O reajuste pode ser aplicado em uma ou várias tabelas de preço simultaneamente **(visão multifilial)**.

**📅 Regras de Período**

* Listagem apenas de períodos **Ativos**.
* Indicação obrigatória por filial vinculada.
* O último reajuste prevalece no mesmo período.
* Bloqueio de reajuste para períodos cronologicamente anteriores a um período que possua reajuste.

🚫

**Bloqueio de Integridade:** Após o reajuste, as matrizes vinculadas à tabela são bloqueadas para qualquer modificação manual, garantindo a fidelidade dos valores calculados.
