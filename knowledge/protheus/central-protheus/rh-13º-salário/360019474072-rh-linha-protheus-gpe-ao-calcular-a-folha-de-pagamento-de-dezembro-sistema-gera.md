---
article_id: 360019474072
category: RH - 13º salário
content_hash: 114f91442525f3cd1d9d53ed9406c5131a2b8681333c1b461332711f10ae214b
fetched_at: '2026-06-28T22:44:00.411617+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Ao calcular a folha de pagamento de dezembro, Sistema
  gera diferença negativa 13º (parâmetro MV_DF13NEG)
type: support-article
updated_at: '2026-06-25T10:46:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019474072-RH-Linha-Protheus-GPE-Ao-calcular-a-folha-de-pagamento-de-dezembro-Sistema-gera-diferen%C3%A7a-negativa-13%C2%BA-par%C3%A2metro-MV-DF13NEG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18737165048727) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao calcular a folha de pagamento gera diferença negativa 13º.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - GPE - Todas as versões  
  
**Solução**  
**Exemplo:**  
Os valores da 2ª parcela foram calculados considerando 12/12 avos. Mas em Dezembro o RH recebeu um atestado com data retroativa de Novembro, fazendo com que o colaborador **perdesse o direito a 1/12 avos de 13° Salario.**  
  
Com isso na folha de pagamento, com as devidas parametrizações (Parâmetro e Mnemônico habilitados), o sistema fez o desconto no ID 0348 - Desconto 13 sal pago a maior.   
O mesmo pode ocorrer quando se trata de faltas superiores a 15 dias no mês de dezembro, ou até mesmo o calculo de Adicionais que incorporavam ao salario no momento do calculo do 13° salario e que por algum motivo após o calculo deixaram de incorporar.

**Como configurar o sistema para gerar automaticamente valores de diferença de 13º. Salário?**

**1.** Habilite o parâmetro **MV\_DF13NEG (S),** via **Módulo Configurador (SIGACFG)** acessando: Base de dados/ Dicionário/ Base de Dados/ pesquise pelo parâmetro/clique em Editar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33632448988183)

**2.** Crie a **verba com ID 0348** – Desconto de diferença 13º Salário em Atualizações/ Definições de cálculo/ Verbas. Veja um exemplo de cadastro na [nesse link.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11222354283927-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-0348-Diferen%C3%A7a-Negativa-13-Salario?source=search)

**Obs:** Se o parâmetro estiver habilitado o sistema pode gerar diferença negativa de bases de INSS e FGTS sobre 13º mesmo que não existe o ID 0348 cadastrado.  
  
**Exemplo:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17849010315031)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17849101664663)**

**Calculo:**  
Salario R$ 3.000,00 / 12 \* 11 = R$ 2.750,00 (o que seria de fato devido de 13° salario)  
Porém a empresa realizou o pagamento de R$ 3.000,00 considerando 12/12 avos.   
Na folha, o sistema calculou o valor pago a maior referente a 1/12 avos , bem como as devoluções de INSS e FGTS que foram recolhidos a maior. 

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17849137055767)**

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como cadastrar o ID 0348 Diferença Negativa 13° Salario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11222354283927-RH-Linha-Protheus-GPE-Como-cadastrar-o-ID-0348-Diferen%C3%A7a-Negativa-13-Salario?source=search)  
[RH - Linha Protheus - GPE - Complemento 13º negativo impede a transmissão do S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062332213-RH-Linha-Protheus-GPE-Complemento-13%C2%BA-negativo-impede-a-transmiss%C3%A3o-do-S-1200?source=search)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410720423959-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionados-ao-c%C3%A1lculo-do-complemento-de-13%C2%BA)
