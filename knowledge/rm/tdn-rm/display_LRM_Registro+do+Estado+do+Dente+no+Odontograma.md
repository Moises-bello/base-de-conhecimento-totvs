---
content_hash: abb41a4bea802afae0f37d579c99033352802ce319db37f4454be7c458ad8574
fetched_at: '2026-06-29T00:12:14.656711+00:00'
page_id: '969580938'
product: rm
source: tdn-rm
title: Registro do Estado do Dente no Odontograma
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+do+Estado+do+Dente+no+Odontograma
version: 9
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Descrição da Funcionalidade**
3. **Interface da Tela**
4. **Estados clínicos para a seleção**
5. **Funcionalidade da Marcação do Dente**
6. **Módulos Envolvidos**

sumarioVisão Geral

## **01. VISÃO GERAL**

### **Objetivo**

Permitir que o dentista registre de forma padronizada e precisa o **estado clínico de um dente** diretamente pelo odontograma, com base nas opções previamente cadastradas, facilitando o diagnóstico e a definição dos procedimentos a serem realizados.

Descrição da Funcionalidade

## **02. Descrição da Funcionalidade**

Ao clicar sobre um dente na tela do **Odontograma**, será exibida a interface de **“Realizar Marcação”**, onde o profissional poderá:

* Confirmar o dente selecionado
* Definir o **estado clínico**
* **Incluir procedimentos e informações financeiras**
Interface da Tela

## **03. INTERFACE DA TELA**

### **Interface da Tela**

**Componentes da tela:**

**Dente:** Exibe o número e nome do dente selecionado. Exemplo: *"16 - Primeiro Molar Superior Direito"*.

**Estado do dente:** Caixa de seleção com os estados previamente cadastrados. Exemplo: *Hígido, Restaurado, Extraído*.

**Procedimentos:** Permite associar procedimentos odontológicos ao dente selecionado.

**Face:** Habilitado conforme o procedimento, define as áreas afetadas do dente.

**Convênio | Plano | Procedimento | Quantidade | Valor Unitário e Total:** Usado para registrar informações financeiras, caso necessário.

**Observações:** Campo livre para incluir informações adicionais ou notas clínicas.

**Critérios de Aceitação**

**Exibição da tela:** Ao clicar em qualquer dente no odontograma, a tela “Realizar Marcação” deve ser exibida.

**Identificação do dente:** O campo “Dente” deve trazer o número e nome completo automaticamente.

#### **Persistência dos dados:** Após salvar, o estado do dente é refletido visualmente no odontograma (cor no dente).

Estados Clínicos para Seleção no Odontograma

## **04. QUAIS ESTADOS CLÍNICOS ESTÃO DISPONÍVEIS PARA SELEÇÃO NO ODONTOGRAMA?**

* Hígido (cor padrão/default)
* Restaurado (verde)
* Cariado (vermelho)
* Extração Indicada (roxo)
* Ausente (somente contorno)
* Implante (azul)
* Tratado Endodonticamente (azul escuro somente a raiz)

Fluxo da Tela

## **05. Funcionalidade da Marcação do Dente**

Ao clicar sobre um dente na tela do **Odontograma**,

será exibida a interface de **“Realizar Marcação”**,

**onde o profissional poderá:**

* Confirmar o dente selecionado.
* Definir o estado clínico do dente.
* Definir a(s) face(s) do(s) dente(s).
* Incluir procedimentos e informações financeiras.
* Incluir observações se necessário.

## **É possível alterar o estado do dente depois de marcado?**

Sim. Você pode clicar novamente no dente e selecionar um novo estado a qualquer momento. A nova cor será aplicada imediatamente, sem necessidade de limpar ou desfazer o anterior.

## **As marcações são salvas automaticamente?**

Sim. Todas as marcações realizadas são salvas automaticamente no prontuário odontológico do paciente. Ao acessar novamente o odontograma, os dados já estarão carregados.

Módulos Envolvidos

## **06. MÓDULOS ENVOLVIDOS**

* Odontograma
* PEP Odontológico
* Cadastro de Estados de Dentes
* Procedimentos Odontológicos

### **Benefícios**

* Registro clínico mais rápido e intuitivo
* Redução de erros de marcação
* Integração com procedimentos e convênios
* Visibilidade clara da situação bucal do paciente
