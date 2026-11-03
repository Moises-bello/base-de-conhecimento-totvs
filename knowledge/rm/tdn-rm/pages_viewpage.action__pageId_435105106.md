---
content_hash: 5fb1e0998440a08b9966d992e31b93fe5ce9e8e3e60a2e56a953dabacd8f33de
fetched_at: '2026-06-29T00:09:47.936982+00:00'
page_id: '435105106'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Alteração de Garantias do Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105106
version: 9
---

O aditivo de Garantia do Contrato tem o objetivo de permitir a troca do Tipo de Garantia em um Contrato de Locação Efetivado.Inicialmente  o aditivo será criado com o status 'Preparação' e requer que o processo  Efetivar seja executado  e assim  ele seja aplicado sobre o contrato efetuando as devidas alterações.

**Pré-Condições:**

* Ter habilitado a permissão [02.03.01.12 e 13] para Efetivar / Desfazer aditivo de Alteração de Garantias do Contrato, do perfil do TOTVS Gestão de Imóveis, localizada em *Serviços Globais / Segurança / Perfis.*
* Ter Efetivado o Contrato de Locação.
* Ter incluído um [Motivo do Aditivo] do tipo 'Garantia'.

**Incluindo um Aditivo de Troca de Garantia**

* Após selecionar um Contrato que atenda  a pré-condição 1, acesse: Anexos/Aditivo/Garantia do Contrato;
* Clique em Incluir Aditivo de Garantia do Contrato;
* Preencher os campos conforme desejar. Os campos exibidos na tela são:

* + - Código do Aditivo
    - Data do Aditivo
    - Tipo de Aditivo
    - Situação do Aditivo
    - Motivo do Aditivo
    - Número do Aditivo no Cliente: Campo onde o cliente informar o número do Aditivo no Contrato físico. Podendo assim realizar o agrupamento de vários aditivos do sistema a um aditivo físico.
    - Modalidade de Garantia Anterior
    - Nova Modalidade de Garantia:

* + - * Caução- Habilita a aba Garantias Financeiras
      * Carta Fiança- Habilita a aba Garantias Financeiras
      * Seguro Fiança- Habilita a aba Garantias Financeiras
      * Título de Capitalização- Habilita a aba Garantias Financeiras
      * Fiador- Habilita a aba Garantias Fiadores
      * Sem Garantia - Não habilita as abas Garantias Financeiras e Garantias Fiadores.
      * Cessão Fiduciária - Habilita a aba Garantias Financeiras

Clique em Salvar para adicionar o Aditivo  que será criado com o status 'Preparação'

Se foi selecionada uma Modalidade de Garantia diferente de Sem Garantia  os dados de sua respectiva aba deve ser preenchido.

**Garantias Financeiras**

* **Pré-Condições**
  + Ter selecionado uma das Modalidades de Garantia:

* + - Caução
    - Carta Fiança
    - Seguro Fiança
    - Título de Capitalização
    - Cessão Fiduciária

* **Preenchendo a aba Garantias Financeiras**
  + Clique em Adicionar Garantia Financeira
  + Preencher  os campos.

* + - Identificador da Garantia Anterior
    - Novo Número da Garantia
    - Nova Instituição
    - Novo Valor Total da Garantia
    - Nova Situação da Garantia
    - Nova Data de Pagamento
    - Nova Validade Inicial
    - Nova Validade Final
    - Nova Observação da Garantia

* + Clique em Salvar
  + O sistema permite Editar os dados inseridos ou Excluir o registro incluído anteriormente

**Garantias Fiador**

* **Pré-Condições**
  + Ter selecionado a  Modalidade de Garantia: Fiador

* **Preenchendo a aba Garantias Fiadores**  
  + Clique em Adicionar Garantia Fiador
  + Preencher  os campos.

* + - Identificador Fiador Anterior;
    - Data inicial e Data Final Anterior - Preenchido automaticamente se houver Fiador Anterior;
    - Novo Fiador;
    - Nova Data Inicial e Final - Preenchido automaticamente com o período de vigência do Contrato;

* + Clique em Salvar;
  + O sistema permite Editar os dados inseridos ou Excluir o registro;
  + Efetivar o Aditivo;
  + Verifique que o status do Aditivo foi alterado para Efetivado;
  + Selecione o Aditivo e clique em Editar Aditivo de Troca de Garantia;
  + Acesse a aba Histórico. Será exibida a informação  do campo Observação preenchido ao efetivar o Aditivo.

Importante

* Se o contrato possui uma garantia associada com vinculo ao valor do contrato, (opção "Vínculo com o valor do contrato" no cadastro de garantias), o sistema exigirá, na efetivação dos aditivos de alteração / exclusão de imóveis, um aditivo de garantia em preparação para ser aplicado. Este aditivo será automaticamente efetivado ao se efetivar o aditivo de troca de imóvel / exclusão de imóvel;
* Os aditivos de alteração / exclusão de imóvel deverão possuir o mesmo número do aditivo de garantia "Em Preparação" para que sejam efetivados corretamente;
* Da mesma forma, ao desfazer os aditivos de alteração / exclusão de imóvel, o sistema automaticamente deverá desfazer o aditivo de garantia e voltar sua situação para "Em Preparação".
