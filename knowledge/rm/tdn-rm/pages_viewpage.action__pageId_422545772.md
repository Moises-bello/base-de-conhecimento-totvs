---
content_hash: f64fc2b72fdb2a60288849f289c1f8d100663056042a1bd510ccfc12f135895c
fetched_at: '2026-06-29T00:09:21.032319+00:00'
page_id: '422545772'
product: rm
source: tdn-rm
title: Período Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545772
version: 6
---

**Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

O Cadastro de Período Fiscal será definido pelo usuário responsável considerando o intervalo entre a abertura e o fechamento do período para lançamentos e ou alterações nos livros fiscais.  
O Fechamento do Período Fiscal moverá a base desse período para as Tabelas Históricas, liberando espaço na base original para os próximos lançamentos, melhorando a performance do sistema.  
  Na criação do período fiscal o status deverá ser "aberto";

* Período fiscal com o status "fechado" não poderá ter registros manipulados;
* Na criação do período, a data final não poderá ser menor que a data inicial;
* Não poderá ser incluído mais de um período com o mesmo intervalo de datas;
* Ao cadastrar um período com datas iguais o sistema deve apresentar uma mensagem informando o erro;
* Períodos Fiscais Fechados não poderão ser excluídos e nem alterados;
* Na exclusão de algum registro todos os logs referentes a ele deverão ser excluídos;
* Os intervalos das datas do período fiscal deverão ser anuais e toda alteração processada terá um log.

**Novidades**

* Efetuada melhoria no processo de Fechamento/Abertura do período fiscal para que seu processamento interno ocorra mês a mês. Tal implementação impede que o log de transação do banco fique cheio a ponto de suspender a execução do processo.
* Implementados os status "Aberto parcial" e "Fechado parcial". Um período fiscal ficará com status Aberto/Fechado parcial quando ocorrer problema durante o fechamento ou abertura dele e já tenha ocorrido o processamento de pelo menos um mês.
* Efetuada melhoria nas rotinas fiscais EFD Contribuições, SPED Fiscal, ECF – Escrituração Contábil\Fiscal, TAF, DAPI, SINTEGRA para não serem geradas quando suas datas de geração estiverem compreendidas dentro de um período fiscal aberto/fechado parcial.

**Fechamento do Período Fiscal**

O Fechamento do Período Fiscal consiste em mover toda a base dos registros fiscais de um determinado período para as tabelas históricas.  
O objetivo é de otimizar o banco de dados e melhorar a performance do sistema, uma vez que todos os registros do período fechado estarão em outra tabela.  
Para executar o Fechamento de Período Fiscal selecione um cadastro com status do período fiscal "Aberto" e execute o Processo "Fechar Período Fiscal".  
Após o fechamento do Período Fiscal, a documentação fiscal ficará disponível apenas para consulta, não sendo permitido quaisquer alterações.  
Será gerado um log referente a cada fechamento realizado.  
  
**Reabertura do Período Fiscal**

A reabertura do Período Fiscal consiste em mover de volta toda a base dos registros fiscais das tabelas históricas de um determinado período para as tabelas originais. O objetivo é de liberar os registros para possíveis manipulações. Para executar a reabertura do Período Fiscal selecione um cadastro com status do período fiscal "Fechado" e execute o Processo "Abrir Período Fiscal". Após a Reabertura do Período Fiscal, a documentação fiscal ficará disponível para quaisquer manipulações. Será gerado um log referente a cada Reabertura realizado.

---
