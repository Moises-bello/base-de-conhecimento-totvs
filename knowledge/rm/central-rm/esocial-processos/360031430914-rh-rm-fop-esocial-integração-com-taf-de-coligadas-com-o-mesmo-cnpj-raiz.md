---
article_id: 360031430914
category: esocial - Processos
content_hash: 85240e8882ffccd8ae2ceb2649ac78f0c27beecf49bd65bd2328698f779e17a1
fetched_at: '2026-06-28T22:47:08.386377+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RH - RM - FOP - eSocial - Integração com TAF de coligadas com o mesmo CNPJ
  raiz
type: support-article
updated_at: '2024-07-22T17:20:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031430914-RH-RM-FOP-eSocial-Integra%C3%A7%C3%A3o-com-TAF-de-coligadas-com-o-mesmo-CNPJ-raiz
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25080056958103) Tempo aproximado para leitura: 00:02:30 min  
  
Dúvida**  
Como fazer a integração com TAF quando existe na base de dados mais de uma coligada com o mesmo CNPJ raiz?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
O eSocial exige o envio de informações por empresa. Quando uma filial é cadastrada no sistema como uma coligada, fazendo com que exista mais de uma coligada com o mesmo CNPJ raiz, é necessário realizar determinados procedimentos adicionais.

Foi criado no sistema o parâmetro **Utilizar prefixo para identificação eventos de tabela,** presente em **Configurações | Parametrizador | eSocial | Configurações Gerais 2/7.** Ao marcar esse parâmetro, o campo **Prefixo** e o parâmetro **Utilizar código da coligada como prefixo** serão habilitados. Caso escolher o campo **Prefixo**, os códigos de identificação dos registros no XML serão alterados e em sua frente serão adicionados o valor informado neste campo. Caso escolher o parâmetro **Utilizar código da coligada como prefixo**, o código da coligada será adicionado à frente.

**Exemplos**

* Sem a utilização do prefixo
  1. Parâmetro desmarcado no parametrizador
  2. XML **S-1010** para a rubrica 0001: a TAG **ideTabRubr** retornará o valor **0001**;
  3. XML **S-1020** para a lotação C01S000001: a TAG **codLotacao** retornará o valor **C01S000001**.
* Utilizando o prefixo
  1. Parâmetro marcado no parametrizador e prefixo preenchido com valor **AA**;
  2. XML **S-1010** para a rubrica 0001: a TAG **ideTabRubr** retornará o valor **AA0001**;
  3. XML **S-1020** para a lotação C01S000001: a TAG **codLotacao** retornará o valor **AAC01S000001**.
* Prefixo como código da coligada
  1. Parâmetro marcado no parametrizador e parâmetro **Utilizar código da coligada como prefixo** marcado. Código da coligada: 1
  2. XML **S-1010** para a rubrica 0001: a TAG **ideTabRubr** retornará o valor **10001**;
  3. XML **S-1020** para a lotação C01S000001: a TAG **codLotacao** retornará o valor **1C01S000001**.

Utilizando este recurso, todos os eventos de tabela poderão ser integrados para a mesma **Filial TAF** sem que apresente duplicidade de registro.  
  
**Importante**  
Esse parâmetro será válido para geração dos eventos **S-1010** (**ideTabRubr**) e **S-1020** (**codLotacao**). A soma da máscara da **Lotação Tributária + Prefixo** **Eventos de Tabelas** não poderá ser superior a 30 caracteres.
