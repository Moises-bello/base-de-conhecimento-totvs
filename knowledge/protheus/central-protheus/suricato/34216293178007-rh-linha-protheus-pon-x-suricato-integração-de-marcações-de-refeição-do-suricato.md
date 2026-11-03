---
article_id: 34216293178007
category: Suricato
content_hash: 9444897dfabb2e8b6089901fc6c67c0adc759d1c520853173852eae3d393c1fd
fetched_at: '2026-06-28T22:44:57.274469+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - PON x Suricato - Integração de Marcações de Refeição
  do Suricato
type: support-article
updated_at: '2025-08-15T20:12:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34216293178007-RH-Linha-Protheus-PON-x-Suricato-Integra%C3%A7%C3%A3o-de-Marca%C3%A7%C3%B5es-de-Refei%C3%A7%C3%A3o-do-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34216289644439) Tempo aproximado para leitura: **00:20:00 min**  
  
**Dúvida**  
Como funciona a integração de Marcações de Refeição do Suricato com o Protheus**?**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
A integração do **Protheus x Suricato** acontece através de **parâmetros** e **Webservices,** que anteriormente eram utilizados pelo TSA. Para o bom funcionamento, é necessário garantir que foram efetuadas todas as configurações da documentação: [RH - Linha Protheus - PON x Suricato - Integração Protheus x Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16779731236119-RH-Linha-Protheus-PON-x-Suricato-Integra%C3%A7%C3%A3o-Protheus-x-Suricato)  
  
Garantindo que as integrações estão funcionais, será necessário seguir com as recomendações abaixo:  
  
\*\*Importante relatar de que **as** **marcações de Refeição seguem o mesmo processo utilizado para as marcações de Ponto**, descritas na documentação [RH - Linha Protheus - PON x Suricato - Leitura de Marcações vindas do Suricato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16984496753175-RH-Linha-Protheus-PON-x-Suricato-Leitura-de-Marca%C3%A7%C3%B5es-vindas-do-Suricato)  
  
Durante o processo de importação das marcações da API do SURICATO para API RecordClockMarkings e durante a Pré-leitura (processo que lê as marcações da tabela de integração, RR1, e grava na tabela de Pré-leitura, RFE) não é feita nenhuma distinção entre as marcações de Ponto e de Refeição. Ressalto que isto se aplica aos clientes que ainda utilizam a integração via Banco na tabela MSA\_CONTROL\_MARCAC, ok.

O que determina se a marcação será lida é referenciando se é do relógio de Ponto ou de Refeição é o cadastro do relógio no Protheus, essa informação é utilizada durante o processo de Leitura e Apontamento, na Rotina PONM010, e determina se as marcações são gravadas na SP8 - Marcações ou SP5 - Marcações de Refeição.  
  
Para leitura e gravação das refeições o relógio deverá ser cadastrado conforme orientação abaixo:  
  
**Cadastro do Relógio:**  
  
O campo **Controle**, **P0\_CONTROL**, deve estar preenchido com **R**, para determinar que é um relógio para controle de refeitório.  
  
O campo **REP**, **P0\_REP**, deve estar preenchido, mesmo que o relógio não seja homologado pelas portarias **1510** ou **671**. Essa informação é utilizada para identificar o relógio nas marcações vindas do Suricato, **a mesma informação deve estar presente no Suricato.**

![](https://tdn.totvs.com/download/attachments/976155933/image-2025-8-13_10-19-15.png?version=1&modificationDate=1755091153850&api=v2&effects=drop-shadow)

O campo **Novo Rel**determina onde o sistema irá buscar a informação do campo **P0\_REP** na tabela de integração **RR1**

Novo Rel = 1 - Sim

O sistema busca o conteúdo do campo P0\_REP no campo RR1\_CODREP

Novo Rel = 2 - Não

O sistema busca o conteúdo do campo P0\_REP no campo RR1\_CODREL

O conteúdo do campo irá depender de como as informações foram enviadas pelo Suricato, devendo ser ajustado de acordo.  
![](https://tdn.totvs.com/download/attachments/976155933/image-2025-8-13_10-23-53.png?version=1&modificationDate=1755091434027&api=v2&effects=drop-shadow)  
  
**Cadastro do Funcionário:** Além do **PIS** e/ou **CPF** o funcionário precisa ter o **Crachá**preenchido no cadastro. Isto porquê o sistema valida esta informação e o crachá deverá constar no cadastro de funcionário no Protheus e a mesma informação no Suricato. Exemplo do cadastro de funcionário:  
![](https://tdn.totvs.com/download/attachments/976155933/image-2025-8-13_10-29-33.png?version=1&modificationDate=1755091774247&api=v2&effects=drop-shadow)  
  
Para que o sistema faça a validação correta, leitura e gravação das refeições precisará seguir com as configurações, na documentação abaixo:  
[RH - Linha Protheus - PON - Como efetuar os cadastros das refeições para Leitura no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018129092-RH-Linha-Protheus-PON-Como-efetuar-os-cadastros-das-refei%C3%A7%C3%B5es-para-Leitura-no-Ponto-Eletr%C3%B4nico)  
  
**Saiba Mais:**  
[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)  
[Integração Protheus x Suricato](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546695095)  
[Schedule - Leitura/Apontamento das Marcações](https://tdn.totvs.com/pages/releaseview.action?pageId=631321258)  
[Pacote de Expedição Contínua - Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
