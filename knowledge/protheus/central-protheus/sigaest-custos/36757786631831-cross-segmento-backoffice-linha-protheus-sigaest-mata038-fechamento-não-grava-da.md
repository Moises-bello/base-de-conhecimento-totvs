---
article_id: 36757786631831
category: SIGAEST - CUSTOS
content_hash: 6e233f35568b6764109f21a4327ef16469adca9140154c3c06ac4fdc1bd48e83
fetched_at: '2026-06-28T22:39:00.357399+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - Fechamento
  não grava dados na SB9/SBJ/SBK com procedures ativas
type: support-article
updated_at: '2025-12-03T18:41:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36757786631831-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Fechamento-n%C3%A3o-grava-dados-na-SB9-SBJ-SBK-com-procedures-ativas
---

Durante o fechamento de estoque no Protheus, não são gravados saldos nas tabelas SB9, SBJ e SBK com as procedures instaladas, e aparentemente devido à presença indevida da propriedade Identity com campo R\_E\_C\_N\_O\_. A solução é recriar a tabela sem essa propriedade, garantindo a correta gravação dos saldos iniciais no processo de custos.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36757786621079) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**

Durante o fechamento, com o ambiente atualizado e procedures de 14 a 22 ativas, não é gravado saldos nas tabelas SB9/SBJ/SBK, e isso ocorre apenas com as procedures instaladas, sem as procedure o fechamento concluir a gravação, porque isso acontece?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Apartir da Release 12.1.33.  
  
**Solução**

Possivel ajuste na base de dados em relação as tabelas chave apresentadas.

Durante a execução da etapa de **Fechamento de Estoque (Acompanha Custos / MATA038)**, o sistema finaliza o processamento e atualiza o parâmetro **MV\_ULMES** (Último Mês Fechado), mas **não gera os movimentos de saldos iniciais** nas tabelas:

* **SB9:** Saldos Iniciais
* **SBJ:** Saldos Iniciais por Lote
* **SBK:** Saldos Iniciais por Endereço

### **Usaremos apenas o ALIAS SB9 como referencia, mas isso se aplica as demais SBJ e SBK.**

A falha na gravação dos saldos na tabela **SB9 e demais** durante a execução do processo de custos (que utiliza *Procedures* para *mass-insert*) pode ser causada pela **presença da propriedade Identity com o campo RECNO da tabela**.

![Screenshot_4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36757770349463)

No padrão do Sistema Protheus, a tabela **SB9** **atualmente não possuem Identity** configurado com campo **R\_E\_C\_N\_O\_**, pois o processo de custos insere dados massivamente, dependendo da gestão de sequencialidade do sistema.

Então deve-se avaliar se foi algum UPDDISTR que criou, e caso seja, basta enviar o pacote junto aos dados usados para que o suporte padrão efetue uma averiguação.

A solução para a situação, caso voce tenha até mesmo indices diferentes do apresentado na imagem, bem como o Identity indevido, sera a **Recriação da Tabela SB9** sem a propriedade *Identity* no campo **R\_E\_C\_N\_O\_**.

**Para tal deve-se:**

1. **Backup:** Realizar o *backup* da tabela **SB9**.
2. **Recriação:** Executar o **Drop** e a **Recriação** da tabela **SB9** utilizando a rotina padrão do Protheus (**MATA220 Saldo inicial**) ou via *script* de banco de dados com seu DBA, **garantindo que a coluna R\_E\_C\_N\_O\_ não possua a propriedade Identity**.
3. Após a recriação da tabela, um novo fechamento podera ser realizado, e os saldos agora devem ser gravados corretamente.

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)
