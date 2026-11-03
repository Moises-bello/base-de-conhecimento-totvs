---
article_id: 14626756121367
category: RH - Folha de Pagamento
content_hash: b3d2fb550344d64af36b692e93610aec8f9193d9765b7b7988b0ca717b2af74f
fetched_at: '2026-06-28T22:44:11.875258+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE -  MP-1.171/2023 - Como configurar a nova forma de
  cálculo de IR no Protheus
type: support-article
updated_at: '2025-08-12T12:35:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14626756121367-RH-Linha-Protheus-GPE-MP-1-171-2023-Como-configurar-a-nova-forma-de-c%C3%A1lculo-de-IR-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15272571357335) Tempo aproximado para leitura: **00:02:30 min****Dúvida**MP-1.171/2023 - Como configurar a nova forma de cálculo de IR no Protheus?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Foi publicado no Diário Oficial da União a **[MEDIDA PROVISÓRIA nº 1.171, de 30 de ABRIL de 2023](https://www.in.gov.br/en/web/dou/-/medida-provisoria-n-1.171-de-30-de-abril-de-2023-480184173)**, que altera o cálculo de Imposto de Renda.

Efetuado a alteração no cálculo do IRRF, nos roteiros da 2ª parcela do 13º salário, Adiantamento, Folha, Férias e Rescisão para verificar o desconto simplificado mensal (correspondente a 25% (vinte e cinco por cento) do valor máximo da faixa com alíquota zero da tabela progressiva mensal).

O sistema efetuará o cálculo do IRRF tanto no modelo de tributação completo quanto no modelo de tributação simplificado e irá gerar o desconto de IR de acordo com o modelo de tributação que for mais vantajoso ao empregado, isto é, o que tiver menor valor.

Para atender a nova Medida, é necessário adequar o SIGAGPE, conforme passo a passo a seguir.

**1.** Necessário que o ambiente esteja atualizado com o Pacote >RH Expedição Contínua, liberado a partir do dia 10/05/2023 **(necessário atualização do dicionário e help de campos também):**

**Observações:**

Após atualização com o pacote e dicionário da expedição contínua, pode ser necessário os procedimentos abaixo para carga das atualizações:  
- Entre em Definição tabelas pelo caminho >Atualizações >Definições cálculos >Definição Tabelas, para dar carga nas novas colunas da tabela S002, após isso entre em Manutenção tabelas pelo caminho >Atualizações >Definições cálculos >Manutenção tabelas e verifique se foi atualizada;  
-Entre na rotina Mnemônicos pelo caminho >Atualizações >Definições cálculos >Mnemônicos e verifique se foi criado o mnemônico P\_DEDIRSIM;  
-Entre na rotina de Verbas pelo caminho >Atualizações >Definições cálculos >Verbas e verifique se os IDs foram criados visualizando pelo campo ID p/ cálculo.  
-Verifique se os campos \_TRIBIR foram criados nas tabelas RGB, SRC, SRD e SRR. Se por algum motivo não foram criados, é possível efetuar a criação manual dos campos abaixo, via módulo Configurador:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14625411492247)

**Documentação Técnica:**  
[https://](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638)[tdn.totvs.com/pages/releaseview.action?pageId=756458638](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638)

**2.** Necessário atualização das novas informações na Tabela S002 em >Atualizações>Definições Cálculo>Manutenção de Tabelas:

Efetuado alteração na tabela auxiliar S002 (tabela de imposto de renda),  criado o campo "Dedução Simplificada", onde deverá ser informado o valor do desconto simplificado mensal de **R$ 528,00** e o campo "Calc. Novo?", onde deverá ser preenchido com **"S"** (sem aspas) caso a linha digitada seja referente ao cálculo alterado pela MP.

* Exemplo de preenchimento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14626281257751)

**Dica**  
Na tabela auxiliar S002 (Tabela de Imposto de renda) , altere a linha referente ao ano 2023 preenchendo no campo "Ano/Mês Fin." o período de "202304" (sem aspas) e inclua uma nova linha com o campo "Ano/Mês Ini." preenchido com "202305" (sem aspas).

**Observação**  
Quando o período de início for a partir de 202305, o campo "Calc. Novo?" virá preenchido automaticamente com "S".

**Importante**

A Atualização da tabela S002 -Tabela de Imposto de renda, deve ser realizada logo após a atualização da expedição contínua, e antes do processamento dos cálculos com a aplicação da Medida Provisória.

**3.** Para tornar visível qual o modelo de tributação foi mais vantajoso, o sistema irá gravar o indicativo do modelo de tributação **na verba do desconto do IR nos novos campos \_TRIBIR**, sendo "1" (sem aspas) para o modelo de tributação completo, e "2" (sem aspas) para o modelo de tributação simplificado.

* Exemplo de preenchimento nos cálculos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14626886334359)

**4.** Para auxiliar na conferência dos cálculos, foi efetuada a criação dos identificadores de cálculo 1913 a 1924:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14627116469271)

**Dica**

Todos os IDs acima são para auxílio na conferência do cálculo, portanto não são obrigatórios.

Caso deseje cadastrá-los, deverão ser criadas verbas do tipo de código "4" (Base (Desconto), sem quaisquer incidência para folha e e-social (verificar qual código vigente no leiaute atual, para Rendimento com tributação isenta), Natureza e-social informativa "9989" (verificar possíveis alterações na vigência da natureza no leiaute atual do e-social).

**Saber Mais:**

FAQ da Consultoria de Segmentos:

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181>

<https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/>

[DOU - MEDIDA PROVISÓRIA nº 1.171, de 30 de ABRIL de 2023](https://www.in.gov.br/en/web/dou/-/medida-provisoria-n-1.171-de-30-de-abril-de-2023-480184173)
