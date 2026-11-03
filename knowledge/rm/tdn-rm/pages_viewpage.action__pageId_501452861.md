---
content_hash: a712a5eca311cd95daea9898fdf169d14a2b502ab04852339fed7a7f18b91010
fetched_at: '2026-06-29T00:10:25.039976+00:00'
page_id: '501452861'
product: rm
source: tdn-rm
title: Como validar diferenças de INSS entre RM e Governo em caso de Férias Partidas?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501452861
version: 9
---

# Objetivo:

---

       O objetivo deste documento é orientar quais validações são necessárias quando identificado diferença entre o INSS gerado pelo TOTVS Folha de Pagamento e o calculado pelo Governo em casos de férias partidas.

false

**A partir das Versões:**

* + 12.1.22
  + 12.1.23
  + 12.1.24
  + 12.1.25
Passo a Passo1. Evento S-1010

Alguns eventos estão diretamente envolvidos no cálculo de INSS de férias partidas e, por isso, precisam ser validados com bastante atenção. Confira se o XML do S-1010 dos códigos de cálculo de férias estão condizentes com as informações abaixo relacionadas:

**[Código de Cálculo 41 - Férias no Mês](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452718570)**  
**tpRubr**: 1 (Provento)  
**codIncCP**: 11

**[Código de Cálculo 42 - Férias no Próximo Mês](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452718562)**  
**tpRubr**: 1 (Provento)  
**codIncCP**: 00

**[Código de Cálculo 44 - Férias Pagas no Mês Anterior](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452718568)**  
**tpRubr**: 3 (Base de Cálculo)  
**codIncCP**: 11  
  
  
**[Código de Cálculo 76 - 1/3 Férias no Mês](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719012)**  
**tpRubr**: 1 (Provento)  
**codIncCP**: 11 (caso incida INSS) ou 00 (caso não incida)

**[Código de Cálculo 82 - INSS Férias](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452718205)**  
**tpRubr**: 2 (Desconto)

**- Recibo**: Substituído no XML pelo campo "[Evento Antecipação de Férias(Desconto)](https://tdn.totvs.com/pages/viewpage.action?pageId=645896860)" do parametrizador.  
**codIncCP**: 00

**- Encelope**: Substituído no XML pelo campo "[Evento INSS Férias envelope](https://tdn.totvs.com/pages/releaseview.action?pageId=540899121)" do parametrizador.  
**codIncCP**: 31

**[Código de Cálculo 130 - INSS Férias Próximo Mês](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452718229)**  
**tpRubr**: 2 (Desconto)  
**codIncCP**: 00

**[Código de Cálculo 131 - INSS Férias Desconto Mês Anterior](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452718225)**  
**tpRubr**: 4 (Base de Cálculo Dedutora)  
**codIncCP**: 31

2. Eventos no RET

Importante também validar se as incidências no ambiente do Governo estão de acordo com as enviadas pelo ERP origem. Podem ocorrer diferenças devido à alterações diretamente no TAF ou no próprio RET.

Desta forma, acesse o eSocial Web e em **Empregador | Tabelas | Tabela de Rubricas** verifique se os eventos citados na etapa anterior estão corretamente informados. Verifique também se o período de início de validade desta rubrica engloba o período de apuração utilizado no S-1200.

Caso necessário ajustar alguma rubrica, utilize os processo de alteração ou retificação dos eventos de tabela.

3. XML S-1200

Garantindo a consistência das informações das verbas entre TOTVS e Governo, será necessário validar os valores gerados no S-1200.

Lembrando que para empresas que trabalham com Tomadores de Serviços, o XML do S-1200 é gerado considerando o rateio realizado através da distribuição do SEFIP..

Valide se os valores do envelope (ou da distribuição do SEFIP), estão corretos no XML S-1200. Para isto, pode-se realizar a conferência manual ou executar **Processos | Validar S-1200 com Envelope** presente em **Eventos da Folha**.

Se necessário ajuste do XML, utilize o processo de [retificação da Folha](http://tdn.totvs.com/pages/viewpage.action?pageId=491459434).

4. XML S-5001

Considerando agora que as incidências e os valores gerados para cada verba no XML estão corretos, deve-se validar o retorno dado pelo governo através do S-5001.

Utilizaremos como **exemplo** um funcionário com **férias partidas** entre os meses de **Agosto e Setembro de 2018**. Clique nos meses abaixo para expandir as informações de cada mês.

Agosto/2018

**Envelope de Pagamento**

No envelope abaixo é possível verificar que a **base de INSS do mês** gerado pelo RM é de **R$24.636,36**, correspondente à **1/3 Férias no mês** (3.992,42) + **Férias no mês** (11.977,27) + **Dias Trabalhados** (8.666,67). Note que as verbas relativas à **Férias no Próximo Mês** não entram no cálculo de base de INSS deste mês, apesar de ocorrer o desconto do **INSS Próximo Mês** no envelope.

**S-5001**

No S-5001 de Agosto/2018 retornado pelo governo após transmissão do S-1200 apresenta o valor da **Base de Cálculo da Contribuição Previdenciária Normal** como **R$ 24.636,36**, valor idêntico ao calculado pelo RM. Além disso, também é apresentado **R$ 621,03** como **Valor Total Descontado do Trabalhado para Recolhimento à Previdência Social**. Este valor é composto no RM pelas verbas **INSS Férias** (351,92) + **INSS Folha** (269,11).

É possível verificar também que o Valor Segurado (calculado pelo governo) e o Valor Descontado do Segurado (enviado pelo RM) também são iguais, visto o correto envio de informações.

Setembro/2018

**Envelope de Pagamento**

No envelope abaixo de Setembro/2018, segundo mês das férias, serão lançados os eventos de base de cálculo relativos à Férias mês Anterior. Em nosso exemplo, não realizamos o lançamento da Folha neste mês. Assim, a **base de INSS** relativa à 09/2018 é **R$12.212,12**, correspondente à **1/3 Férias Pagas Mês Anterior** (3.053,03) + **Férias Pagas no Mês Anterior** (9.159,09).

**S-5001**

No S-5001 de Setembro/2018 retornado pelo governo após transmissão do S-1200 apresenta o valor da **Base de Cálculo da Contribuição Previdenciária Normal** como **R$ 12.212,12**, valor idêntico ao calculado pelo RM. Além disso, também é apresentado **R$ 621,03** como **Valor Total Descontado do Trabalhado para Recolhimento à Previdência Social**. Este valor é composto no RM pelas verbas **INSS Férias** (269,11) + **INSS Folha** (351,92).

É possível verificar também que o Valor Segurado (calculado pelo governo) e o Valor Descontado do Segurado (enviado pelo RM) também são iguais, visto o correto envio de informações.
