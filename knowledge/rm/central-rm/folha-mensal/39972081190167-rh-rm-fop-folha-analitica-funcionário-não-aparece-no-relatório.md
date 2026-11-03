---
article_id: 39972081190167
category: Folha Mensal
content_hash: e00a03ae067269808ef52f86da2e63329cddea0d5f8e8ccb01c3481e04190518
fetched_at: '2026-06-28T22:46:57.929085+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Folha Analitica - Funcionário não aparece no relatório
type: support-article
updated_at: '2026-04-23T21:57:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39972081190167-RH-RM-FOP-Folha-Analitica-Funcion%C3%A1rio-n%C3%A3o-aparece-no-relat%C3%B3rio
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39972081177623) Tempo aproximado para leitura: 00:10:00 min  
  
**Dúvida**  
Na geração da Folha Analitica alguns funcionários não estão aparecendo, fazendo com que as bases fiquem diferentes do eSocial.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**  
Para a situação em questão, inicialmente é necessário identificar quais funcionários não estão sendo apresentados no relatório.

Durante a geração do relatório, na etapa de seleção de coligada, é possível aplicar filtros ou realizar a geração para um funcionário específico, conforme exemplificado no material de apoio (print).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39972089241111)

### **Validação de Parâmetros de Geração**

Neste momento, já é possível identificar uma das causas mais comuns: inconsistência nos parâmetros de seleção utilizados na geração do relatório.

Deve-se verificar se os seguintes itens estão corretamente marcados:

* Situação do funcionário
* Tipo de funcionário
* Tipo de recebimento

**Exemplo:**  
Caso um funcionário esteja com:

* Situação: Ativo
* Tipo de recebimento: Mensalista
* Tipo de funcionário: Comissionista

E, durante a geração, a opção correspondente a “Comissionista” não esteja selecionada, este funcionário não será considerado no relatório.

---

### **Validação por Funcionário**

Após identificar o(s) funcionário(s) não apresentados, recomenda-se gerar o relatório individualmente para cada um e verificar se há retorno de mensagem de erro.

Caso seja exibida a mensagem *“Nenhum funcionário atende à seleção”*, seguir as validações abaixo:

---

### **Caso 1: Inconsistência de Históricos na Data de Admissão**

Verificar se existem registros válidos, na data de admissão, nos seguintes históricos:

* Histórico de Situação
* Histórico de Seção
* Histórico de Função
* Histórico Salarial

**Possíveis inconsistências:**

* Ausência de registro na data de admissão
* Registro existente com data divergente da admissão

**Ação recomendada:**  
Criar ou ajustar os históricos, conforme o cenário, garantindo que exista registro válido na data de admissão do funcionário.

---

### **Caso 2: Funcionário Transferido (Período Anterior à Transferência)**

Quando o funcionário foi transferido, é necessário observar a data de geração da folha analítica.

Se o relatório estiver sendo gerado para uma competência anterior à transferência, o correto é realizar a geração considerando a **chapa anterior**, e não a atual (criada após a transferência).

---

### **Caso 3: Funcionário Transferido na Competência Atual**

Quando a geração ocorre na mesma competência da transferência, é necessário garantir que o funcionário possua eventos lançados no:

* Envelope
* Ficha Financeira

Em alguns cenários, a ficha financeira não é automaticamente carregada para a nova chapa, devido a parametrizações aplicadas no processo de rescisão/transferência.

**Ação recomendada:**

* Realizar a exportação da ficha financeira da chapa de origem
* Efetuar a importação na chapa atual

Conforme procedimentos descritos nas documentações:

[RH - RM - FOP - Exportação da ficha financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9189246452247-RH-RM-FOP-Exporta%C3%A7%C3%A3o-da-ficha-financeira)

[RH - RM - FOP - Importação da Ficha Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037641813-RH-RM-FOP-Importa%C3%A7%C3%A3o-da-Ficha-Financeira)

### **Observação: Geração por Centro de Custo**

Caso a folha analítica esteja sendo gerada por centro de custo, é necessário validar:

1. Acessar o envelope do funcionário
2. Verificar se os eventos estão distribuídos por centro de custo

Se não estiverem:

* Validar se o rateio de centro de custo está corretamente vinculado ao funcionário
* Recalcular o envelope para que os eventos sejam redistribuídos corretamente

**Saiba mais:**

[**RH - RM - FOP - Folha Analítica por seção**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27567276229015-RH-RM-FOP-Folha-Anal%C3%ADtica-por-se%C3%A7%C3%A3o)

[**RH - RM - FOP - Folha Analítica por centro de custo**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13856176387735-RH-RM-FOP-Folha-Anal%C3%ADtica-por-centro-de-custo)

[**RH - RM - FOP - Relatórios: Nenhum funcionário atende à seleção**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009848672-RH-RM-FOP-Relat%C3%B3rios-Nenhum-funcion%C3%A1rio-atende-%C3%A0-sele%C3%A7%C3%A3o)

[**RH - RM - FOP - Funcionários demitidos não aparecem na folha analítica**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026216773-RH-RM-FOP-Funcion%C3%A1rios-demitidos-n%C3%A3o-aparecem-na-folha-anal%C3%ADtica)
