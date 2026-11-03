---
article_id: 38486359011351
category: Contabilidade Gerencial - Conciliador BackOffice
content_hash: 15f69343fdebb5557c73fa3162290b57af97ef58de78842997284412f1a92bbf
fetched_at: '2026-06-28T22:40:30.971108+00:00'
product: protheus
section_id: 31314114896791
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA940 - Conciliador
  não realiza o match automático
type: support-article
updated_at: '2026-02-23T19:40:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38486359011351-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-n%C3%A3o-realiza-o-match-autom%C3%A1tico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38486358986135) Tempo aproximado para leitura: 00:15 min  
  
**Dúvida**  
Por que o conciliador contábil não realiza o match (interligação) automático dos lançamentos, mesmo existindo movimentos ?  
  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.1.33  
  
  
**Solução**  
Para que a conciliação automática ocorra com sucesso, o sistema cruza as informações da **Tabela de Origem** definida no Setup do Conciliador com a **Tabela de Origem** gravada no Rastreamento Contábil (CV3).

O sistema não realiza o match automático se houver divergência entre o que o Conciliador "espera" e o que a Contabilidade "entregou". Isso ocorre quando a contabilização é gerada em uma tabela diferente daquela configurada para conciliação.

🔽 Cada Processo de Conciliação (Setup) possuí uma tabela específica
do Protheus, que será comparada com a CT2 (lançamentos contábeis) clique
e veja mais.

| SETUP | Tabelas Comparadas |
| --- | --- |
|
| 0001-Contas a Receber x Contabilidade | CT2 X SE1 |
| 0002-Contas a Pagar x Contabilidade | CT2 X SE2 |
| 0003-Movimentação Bancária x Contabilidade | CT2 X SE5 |
| 0004-Cabeçalho das NF de Entrada x Contabilidade | CT2 X SF1 |
| 0005-Itens das NF de Entrada x Contabilidade | CT2 X SD1 |
| 0006-Movimentações Internas x Contabilidade | CT2 X SD3 |
| 0007-Pedidos de Compras x Contabilidade | CT2 X SC7 |
| 0008-Cotações x Contabilidade | CT2 X SC8 |
| 0009-Pedidos de Venda x Contabilidade | CT2 X SC5 |
| 0010-Itens de Pedidos x Contabilidade | CT2 X SC6 |
| 0011-Cabeçalho NF Saída x Contabilidade | CT2 X SF2 |
| 0012-Itens NF Saída x Contabilidade | CT2 X SD2 |
| 0013-Cheques x Contabilidade | CT2 X SEF |
| 0014-Rateio NF Saida x Contabilidade | CT2 X AGH |
| 0015-Rateio Pedido de Venda x Contabilidade | CT2 X AGG |
| 0016-Mov AVP CR x Contabilidade | CT2 X FIP |
| 0017-Distrib de Naturezas em CC x Contabilidade | CT2 X SEZ |
| 0018-Mov AVP CP x Contabilidade | CT2 X FIS |
| 0019-Movimentos do Caixinha x Contabilidade | CT2 X SEU |
| 0020-NF de Entrada x Contabilidade | CT2 X SF1 |
| 0021-NF de Saída x Contabilidade | CT2 X SF2 |
| 0023-Conciliação Bancária Automática | Esta conciliação não utiliza movimentos da contabilidade, para detalhes contatar o módulo financeiro! |
| 0024-Conciliação Bancária Manual | Esta conciliação não utiliza movimentos da contabilidade, para detalhes contatar o módulo financeiro! |

* Se o seu Setup de conciliação está configurado para olhar a tabela **X**;
* Mas a contabilização foi feita utilizando um Lançamento Padrão (LP) que olha para a tabela **Y**;
* **Resultado:** O sistema buscará o ID de rastreamento na tabela X, mas ele só existe na tabela Y. O vínculo não é encontrado.

**Cenário comum - Interligação Compras x Financeiro:**  
Setup: 0002 - Contas a pagar x Contabilidade.  
  
Quando a contabilização ocorre na entrada da NF (Compras) e não na geração do título (Financeiro), o conciliador de Contas a Pagar não consegue localizar o destino esperado, pois está buscando referência na SE2, mas a contabilização foi realizada com base na SD1/SF1, assim o sistema não encontra referência, não realizando o match.

Esse comportamento é estrutural e não é considerado erro, apenas conceito de busca de informações.

🔽 Clique para visualizar um exemplo prático de erro comum:

▪️Configuração do Conciliador:
**O usuário seleciona o processo Contas a Pagar
(Processo 002).**  
Esse processo realiza a busca de registros na **tabela SE2** (Títulos
a Pagar).
Ou seja:  
👉 O conciliador espera encontrar movimentações cuja origem esteja vinculada
ao Financeiro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38486358987671)

  
▪️ Contabilização Realizada:  
A contabilização foi configurada para ocorrer na **Entrada da Nota Fiscal (Lançamento
Padrão de Compras - Ex: LP 650).**  
Neste caso, a origem da contabilização gravada na tabela **CV3** é
a **SD1 (Itens
da Nota) e não a SE2.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38486365308823)

  
  
▪️ Análise da discrepância apresentada:  
Na tela do conciliador, o lote contábil exibido refere-se ao
**módulo de Compras (exemplo: Lote 008810)
e não ao módulo Financeiro (exemplo: Lote 008850).**  

O que acontece na prática:  
🔹O conciliador (Processo 002) tenta cruzar dados da SE2  
🔹A contabilização existente está vinculada à SD1  
🔹Não existe vínculo direto entre esses dois registros

**O cruzamento falha!** O sistema tenta conciliar origens diferentes.

Para identificação dos lotes padrões, verificar a documentação:  
[Lotes de Contabilidade](http://tdn.totvs.com/display/public/PROT/Lotes+de+Contabilidade)

**Como Resolver**

Existem duas formas de corrigir essa divergência, dependendo da necessidade da empresa:

**Opção 1: Ajustar o Processo de Conciliação (Recomendado se a contabilização estiver correta):** Se a contabilização deve permanecer na Entrada da Nota (Compras), você deve utilizar um processo de conciliação compatível.

* Em vez de utilizar o processo "Contas a Pagar" (SE2), utilize o processo **"Itens da NF" (Processo 005)**.
* Isso fará com que o conciliador busque os dados na tabela SD1, permitindo o match automático.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38486358991255)

**Opção 2: Ajustar a Origem da Contabilização:** Se o objetivo é conciliar pelo módulo Financeiro (Títulos), a contabilização não deve ocorrer na Entrada da Nota.

* Desabilite a contabilização na entrada da nota (LP de Compras).
* Configure o Lançamento Padrão para ocorrer na **Inclusão do Título** (LP do Financeiro).  
  [CTBA080 - Configuração de lançamento padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004893562-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA080-Configura%C3%A7%C3%A3o-de-lan%C3%A7amento-padr%C3%A3o)  
    
  Obs: Caso tenha dúvidas sobre a configuração de um LP específico, deve entrar em contato com o time responsável pelo LP para auxílio.
* Dessa forma, a tabela de origem na CV3 passará a ser a SE2, permitindo o match com o processo de Contas a Pagar.

**Caso as configurações acima estejam corretas e o problema persista, realize as seguintes validações técnicas:**

🔽 Validações Técnicas:

#### 1. Compartilhamento de Tabelas (CT2 e CV3)

Verifique se o compartilhamento das tabelas
**CT2 (Lançamentos Contábeis)** e
**CV3 (Rastreamento)** é idêntico.

**Atenção:** Se os níveis de compartilhamento forem
diferentes
(ex: uma exclusiva e outra compartilhada), o sistema poderá apresentar
informações incorretas
ou gerar erros, impedindo o **match**.

**Documentação:**[Como realizar compartilhamento de tabelas no Contabilidade Gerencial (SIGACTB)?](#)

---

#### 2. Preenchimento de IDs (WizardUUID)

Para que a conciliação funcione, os campos de ID (identificadores
únicos)
precisam estar populados nas tabelas de origem, destino e de rastreio.
Caso não estejam, utilize a rotina **WIZARDUUID**:

#### 🔹 Cenário A - IDs não populados

Rode o **WIZARDUUID** na
**Opção 3 (Popular os campos de ID)**
para a data em questão. Isso preencherá o código de ID único
nos registros já gravados.

**Documentação:**[Popular os Campos de ID](#)

  

#### 🔹 Cenário B - Dados não aparecem na aba "Dados da conciliação"

Isso indica que na **CV3** os campos de ID não
foram populados corretamente
ou o lançamento perdeu o vínculo.

Rode o **WIZARDUUID** na **Opção 4**
para a data em questão.
O sistema irá preencher os campos de ID com as informações
do rastreio.

---

#### 3. Integridade do Rastreio Contábil

Se mesmo após os passos anteriores o sistema não realizar o
**match** automático:

* Verifique o rastreio contábil do lançamento específico para garantir
  que ele está apontando para o documento de origem correto.  
  Documentação para auxílio no rastreio:
  [Verificação do Rastreio Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9144446577687-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Exclus%C3%A3o-de-lan%C3%A7amento-cont%C3%A1bil-gera-error-log-Invalid-data-type-on-F3-DTLANC)

---

**Saiba mais:**

[CTBA940 - Conciliador Contábil não traz dados.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9223850384791-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-Cont%C3%A1bil-n%C3%A3o-traz-dados)

[CTBA940 - Conciliador BackOffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451317698583-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-BackOffice)

[Conciliador Protheus - Configuração e Instalação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736)

[Conciliador Backoffice - CTBA940](https://tdn.totvs.com.br/display/public/PROT/Conciliador+Backoffice+-+CTBA940+-+P12+-+Contabilidade+Gerencial)

###
