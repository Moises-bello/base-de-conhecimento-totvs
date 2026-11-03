---
article_id: 32765571785367
category: GESTOR
content_hash: ae1d76325cc5007a2cfcecbc7c426d4a95590719fcbf23edfe3f06ef6f5fa3e6
fetched_at: '2026-06-28T22:44:35.436821+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - Meu RH - O que conferir quando no Meu RH do Gestor, as
  rotinas relacionadas à Gestão não aparecem
type: support-article
updated_at: '2025-08-29T17:44:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32765571785367-RH-Linha-Protheus-Meu-RH-O-que-conferir-quando-no-Meu-RH-do-Gestor-as-rotinas-relacionadas-%C3%A0-Gest%C3%A3o-n%C3%A3o-aparecem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32765609464599) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
O que conferir quando no Meu RH do Gestor, as rotinas relacionadas à Gestão não aparecem  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
Uma possibilidade é quando o Gestor não possui histórico de transferências para aquele departamento superior, responsável pelo Departamento dos funcionários.  
  
O Gestor não poderá ser responsável pelo próprio Departamento que é alocado, ou seja, na prática, o funcionário X não pode estar alocado no Departamento que ele mesmo é o responsável,, ele precisará estar alocado e **transferido** para o Departamento Superior.  
  
Toda requisição do Meu RH, seguirá o fluxo de aprovação cadastrado nos departamentos, para montagem da hierarquia.  
  
A orientação inicial é refazer todos os cadastros de departamentos, da seguinte maneira:

* deletar os campos Matrícula Responsável, Filial Responsável, Empresa Responsável e Departamento Superior de todos esses Departamentos
* salvar todos
* com isso, o QB\_KEYINI será deletado também
* cadastre novamente do topo ao último departamento da hierarquia, preenchendo Matrícula Responsável, Filial Responsável, Empresa Responsável
* **Departamento Superior preencher quando utilizarem a hierarquia por Departamento, pelo MV\_ORGCFG =0**
* **Departamento Superior não preencher quanto utilizarem a hierarquia por Visão Organizacional, pelo MV\_ORGCFG =2**

O parâmetro MV\_ORGCFG é utilizado para, designar qual a forma da estrutura de hierarquia a ser utilizada para as aprovações.   
  
MV\_ORGCFG = 0: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/7917580297623>   
MV\_ORGCFG = 1: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062313494>   
MV\_ORGCFG = 2: <https://tdn.totvs.com/pages/releaseview.action?pageId=557333076>  
  
**A chave de busca que temos no cadastro de departamento (campo QB\_KEYINI).** é de suma importância para essa hierarquia ter a funcionalidade correta, por isso, quando temos um erro ou inconsistência sobre essa questão, a orientação mais eficaz é refazer toda a hierarquia, deletando de forma física o registro o conteúdo das chaves de busca, e excluindo os conteúdos dos campos do departamento via rotina, como Matrícula Responsável, Departamento Superior, Filial e Empresa Responsável.  
  
**Lembrando que, são regras:**

* Se o Departamento cadastrado tiver Departamento Superior, a Matrícula Responsável por aquele Departamento, **obrigatoriamente, precisará estar alocado na SRA no Departamento Superior,** ou seja, nunca, neste caso, um funcionário pode ser responsável pelo próprio Departamento;
* Se o Departamento for o topo da hierarquia, ou seja, não possui Departamento Superior, **não poderá ter Matrícula Responsável em branco, sempre** o Responsável precisa ser um funcionário que está alocado na SRA neste próprio Departamento.

Ao citar alocado é porque precisa ser por **Transferência no GPE, rotina GPEA180**, se inserir o Departamento do funcionário diretamente no banco, **diretamente na SRA, não irá funcionar.**  
  
No mais, a orientação é que seja refeita toda a estrutura, todos os cadastros de Departamentos, validar as transferências dos funcionários e dos Gestores, apoiando-se em nossas documentações, temos diversas delas onde mostramos, passo a passo, com detalhes, as regras e como cadastrar.  
  
**Algumas regras sobre o cadastro dos departamentos.**

* Quando temos um Departamento topo da hierarquia, ou seja, que não possui Departamento Superior cadastrado, o funcionário responsável por ele, precisa ser do mesmo Departamento.
* Quando temos um Departamento com responsável de outro Departamento, precisa cadastrar o Departamento Superior deste funcionário responsável.
* Salvo topo da hierarquia, o funcionário nunca poderá ser responsável pelo próprio Departamento
* Definindo a estrutura de departamentos, não alterar o cadastro diretamente na SRA - tabela de funcionários
* Os funcionários precisarão ser alocados nos novos departamentos, por processo de Transferência
* **Os participantes que serão Gestores, terão um outro usuário do portal com as permissões Meu RH, do Grupo Gestão habilitadas**

[**Não mostra funcionário na Minha equipe quando MV\_ORGCFG=0**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25744857444631-RH-Linha-Protheus-MEU-RH-N%C3%A3o-mostra-funcion%C3%A1rio-na-Minha-equipe-quando-MV-ORGCFG-0)  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
