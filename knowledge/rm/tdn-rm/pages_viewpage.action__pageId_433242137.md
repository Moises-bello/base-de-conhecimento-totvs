---
content_hash: a46f1a1be79cfd4c3ed6950d0ac2f085e7d279d05d2efcd69994896e611c69bf
fetched_at: '2026-06-29T00:09:45.416136+00:00'
page_id: '433242137'
product: rm
source: tdn-rm
title: Cópia de Regras Tributárias Entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=433242137
version: 31
---

## **01. DO PROCESSO**

Disponível **a partir da versão 12.1.31** o processo de Cópia de Regras Tributários Entre Coligadas ocorre conforme regras descritas no cenário abaixo.

* Se não existir um tributo com mesmo código e tipo no destino a cópia do Evento será abortada;
* A cópia será realizada somente para os itens de origem contábil e somente se conta for global ou se existir na coligada de destino;
* O Evento tributário referenciado em algum item como: Atividade Rural ou Lucro da exploração, não será copiado;
* A cópia não permitirá sobreposição;
* Resultado contábil, Lançamento Manual, e Lalur Parte B não serão copiados;
* Os identificadores das tabelas dinâmicas devem ser copiados;
* Os processos, Histórico Padrão, Departamento, Centro de Custo e Filial serão copiados somente se existir no destino. No caso da Filial deve ser avaliado se ela é um item impeditivo, se sim, a copia não será realizada e a situação será logada;
* A seleção de dados da origem já deve prever a cópia de origem Cloud.

## **02.****ONDE ACESSAR**

O processo de Cópia de Eventos Tributários Entre Coligadas pode ser acessado de duas formas:

Em **Gestão Fiscal → Obrigações Principais → Eventos Tributários → Estrutura → Processos → Cópia de Regras Tributárias entre Coligadas**.

ImagemImagem

Em **Serviços Globais** **→ Administração → Cópia de Coligada → Cadastro de Template → Processos → Cópia entre Coligadas**

ImagemImagem

## **03. PARAMETRIZAÇÃO**

Para habilitar a opção do processo de Cópia de Eventos Tributários Entre Coligadas em Gestão Fiscal o primeiro passo é acessar o módulo de **Serviços Globais** **→  Segurança → Perfis**.

Selecionar o perfil atrelado ao usuário desejado, editá-lo e selecionar a aba "Acesso a Menus".

Expandir as opções: **Gestão Fiscal → [02] Obrigações Principais → [02.03.01] Eventos Tributários → (Selecionar esta opção) [02.03.01.01.07] Cópia de Regras Tributárias entre Coligadas.**Clicar em "Permitir Acesso" e  depois em "Salvar".

Imagem

*A próxima etapa a ser descrita é uma parametrização feita somente para exemplificar melhor o conteúdo, **caso ache necessário ou já tenha entidades cadastradas pode pular este processo.***

Para habilitar a opção "Cadastro de Entidades" em "Serviços Globais" o primeiro passo é acessar o módulo de **Serviços Globais** **→  Segurança → Perfis**.

Selecionar o perfil atrelado ao usuário desejado, editá-lo e selecionar a aba "Acesso a Menus".

Expandir as opções: **Serviços Globais → [01] Administração → [01.01.05] Cópia de Coligada → [01.01.05.01] Cadastro de Entidades**. Clicar em "Permitir Acesso" depois em "Salvar".

Imagem

## **05. DA REALIZAÇÃO DO PROCESSO PELO MÓDULO DE GESTÃO FISCAL**

Caso um ou mais Eventos tributários estejam marcados e o processo de Cópia de Regras Tributárias Entre Coligadas seja executado, a seguinte tela irá aparecer.

Neste momento deve(m) ser selecionado(as) para qual(is) coligada(s) a regra deve ser copiada. Após isso, basta clicar em executar.

Imagem

**Observação:** Sobre opção de "Substituir registros no destino se eles já existirem" este processo não permitirá a Sobreposição de Eventos Tributários. A situação será apenas logada pelo processo, e se caso o registro já existir, o mesmo não será sobreposto e caso não existir o mesmo será copiado.

Caso nenhum registro esteja marcado, o sistema irá apresentar a seguinte mensagem:

Como não foi feita nenhuma seleção, você deseja executá-lo para TODOS os **X** registros?

Após clicar em "SIM" a tela de Cópia de Regras Tributárias Entre Coligadas irá aparecer. Caso clique em "NÃO" nada ocorre.

Imagem

## **05. DA REALIZAÇÃO DO PROCESSO PELO MÓDULO DE SERVIÇOS GLOBAIS**

### **05.01 Cadastro de Entidades**

Para exemplificar melhor o processo de cópia no módulo de Serviços Globais foi criado um registro para teste no Cadastro de Entidades. **Caso não necessite, pode pular para o próximo processo.**

Esta opção pode ser acessada em  **Serviços Globais** **→  Administração → Cópia de Coligada → Cadastro de Entidades**.

Imagem

**Configuração do Cadastro de Entidade utilizado no exemplo a seguir:**

**Descrição:** Evento Tributário  
**Action Name:**Não se Aplica  
**Wizard** **Parâmetro:** GlbParamsProcFormCopyColig  
**Server** **Name:** FisCopiaEventoTrbColigadaProc  
**Tabela** **Principal:** DEVCTRB  
**Cód.** **Sistema:** D - Totvs Gestão Fiscal

Imagem

### 05.02 Realizar o processo de Cópia

O processo se resume em selecionar um template cadastrado e realizar o processo de Cópia entre Coligadas.

Imagem

Para exemplificar melhor foi cadastrado um novo Template utilizando a Entidade criada no tópico **05.01**.

Obs.: A cópia também pode ser realizada ao editar a Entidade e ir em **Processos → Cópia Entre Coligadas**.

Imagem

Após selecionado(s) o(s) template(s) deve(m) ser escolhida(s) para qual(is) coligada(s) a regra deve ser copiada. Após isso, basta clicar em executar.

Imagem

O processo também está preparado para cópia de Eventos tributários com origem Cloud.

Imagem
