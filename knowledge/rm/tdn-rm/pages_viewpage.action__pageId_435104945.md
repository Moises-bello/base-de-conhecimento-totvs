---
content_hash: ca5e74f96c3e201871de2ed5d518cc16cd34e8e81b2b88f5f86e1796520f68f3
fetched_at: '2026-06-29T00:09:47.140143+00:00'
page_id: '435104945'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Alteração das regras de reajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104945
version: 18
---

### Introdução

---

O Aditivo de Alteração das regras de Reajuste permite definir novas regras e valores que serão pagos pelo locatário à administradora de imóvel, referentes ao serviço de reajuste do contrato de locação. 

### Procedimentos para utilização

---

* **Pré-Condições:**
  + Ter habilitado a permissão para Efetivar / Desfazer aditivo de Alteração das regras de reajuste, do perfil do TOTVS Gestão de Imóveis, localizada em *Serviços Globais / Segurança / Perfis.*
  + Ter Efetivado o Contrato de Locação.
  + Ter incluído um [Motivo do Aditivo].

* **Incluindo um Aditivo de Alteração das taxas de reajuste:**  
  + Após selecionar um Contrato que atenda as pré-condições acima, acesse: Anexos/Aditivo/Alteração das regras de reajuste.
  + Clique em Incluir Aditivo de Alteração das regras de reajuste

* **Preencher os campos conforme desejar. Os campos exibidos na tela são divididos entre parâmetros do reajuste anterior e novos parâmetros reajuste:**
  + Data do Aditivo: Data da geração do aditivo. Essa data é diferente da data de efetivação.
  + Motivo do Aditivo: Deve ser incluído o motivo neste campo, através do cadastro de motivo.
  + Número do Aditivo no Cliente: Campo onde o cliente informar o número do Aditivo no Contrato físico. Podendo assim realizar o agrupamento de vários aditivos do sistema a um aditivo físico.

* **Novos parâmetros reajuste**
  + Nova fórmula do reajuste: Campo para inserir uma fórmula que realizará o cálculo do reajuste.
  + Moeda: O índice que será utilizado no cálculo do reajuste após efetivação.
  + Nova defasagem cotação: Novo período de defasagem do reajuste.
  + Nova cotação acumulada: Pode ser definido entre índice mensal ou índice acumulado.
  + Nova periodicidade: A periodicidade do novo reajuste será definida neste campo.
  + Nova data de próximo reajuste
  + Deflação novo: Neste campo definimos se o reajuste irá permitir deflação ou se irá ignorar a deflação por período.

Por padrão, todos os valores anteriores serão copiados para os novos valores e então o usuário deve alterar apenas os campos desejados.

Os campos periodicidade e data do próximo reajuste estão relacionadas à data do último reajuste. Portanto ao alterar um campo, o segundo também será alterado automaticamente pelo sistema.

Exemplo - O usuário deseja alterar a data do próximo reajuste de 01/01/2019 para 01/05/2019. A data do último reajuste do contrato é 01/01/2018.

| Regras do reajuste atual | Regras do novo reajuste |
| --- | --- |
| Periodicidade: 12  Data do próximo reajuste: 01/01/2019 | Periodicidade: 16  Data do próximo reajuste: 01/05/2019 |

No exemplo a cima, o sistema informou automaticamente que a periodicidade é igual a 16

**\* Caso não deseje que a nova periodicidade fique automaticamente vinculada à nova data de próximo reajuste basta desmarcar a caixa "Calcular periodicidade baseado na nova data de reajuste" de seleção relativa à esse vinculo e alterar os valores livremente.**

* **Etapas para criação de um aditivo:**
  + Clique em Salvar para adicionar o Aditivo que será criado com o status 'Em Preparação'
  + O sistema permite Editar os dados inseridos ou Excluir o registro
  + Verifique que o status do Aditivo foi alterado para Efetivado.
  + Selecione o Aditivo e clique em Editar Aditivo de Alteração das regras de reajuste, acesse a aba Histórico. Será exibida a informação do campo Observação preenchido ao efetivar o Aditivo.

### **Outros Reajustes**

---

Disponível a partir da versão 12.1.2306 a opção outros reajustes permite ao usuário definir novos parâmetros para os reajustes avulsos cadastrados no contrato de aluguel, como por exemplo o [Reajuste de Condomínio.](https://tdn.totvs.com/pages/viewpage.action?pageId=435104980)

Todas as opções acima listadas se aplicam também a aba "Outros Reajustes", bem como todas as consistências das pré-condições.

Caso o contrato de locação originalmente não possua informações preenchidas na aba "Outros Reajustes" o usuário poderá usar o aditivo para inserir estas novas informações, sem precisar reabrir o contrato.

Os campos que não são passíveis de alteração via aditivo serão sempre considerados de acordo com o o cadastro do reajuste principal no contrato.
