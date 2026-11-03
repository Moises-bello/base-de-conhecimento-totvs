---
article_id: 360057320354
category: RH - 13º salário
content_hash: b4e0667e080f4187876d0d654bf83bf31ac7f38cdf0c14abca31339b3335cff5
fetched_at: '2026-06-28T22:44:00.393903+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - 13º Parcela Única
type: support-article
updated_at: '2026-06-24T19:52:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057320354-RH-Linha-Protheus-GPE-13%C2%BA-Parcela-%C3%9Anica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17960234379159) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**  
Como efetuar calculo de 13º inteiro para o funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Realize os seguintes passos:  
  
1. Em Gestão de Pessoal Acesse: **Atualizações / Definições de Cálculos / Períodos** e cadastre o **Roteiro 132** na competência desejada e mude a coluna **Per.Ativo** para **Sim.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052704916247)  
  
  
2. Acesse rotina de **Cálculo por Roteiro (GPEM020)** através do menu **Miscelânea/ Cálculos/ Por Roteiros** e preencha os parâmetros para cálculo.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052719644823)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052719645719)  
  
Ao clicar em **OK,** será apresentada a tela de Parâmetros do 13º.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052719646871)

**Calcular em Ordem de?:** Informe se a ordem de Processo será por Matricula ou Centro de Custo.

**Data de Referência?:** Informe a Data de Referência para o cálculo. Indicamos preencher sempre com 31/12/XX para que seja considerado 12/12 anos.

**Referência para Média?:** Informe a Data de Referência para cálculo das médias.

**Considera Mês Atual?:** Informe se o mês atual será considerado para composição das médias.

**Verificar Integração?:** Informe se há integração dos módulos Faturamento e/ou Financeiro.

**Receita De? e Receita Até?:** Informe o intervalo de datas que serão utilizados para busca das receitas nos módulos Faturamento e/ou Financeiro. (Observação: Só devem ser preenchidas se a pergunta "Verificar Integração?” for preenchida com Sim)

3. Para gerar o relatório de conferência acesse: **Relatórios > Periódicos > Folha de Pagamento.** Em **Outras Ações** selecione **Parâmetros**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052704927767)**  
  
  
  
Preencha os Parâmetros  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052719650455)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052719652247)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052719653527)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052704936215)  
  
Clique em **IMPRIMIR**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052719654807)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052704938391)**  
  
**IMPORTANTE:**  
O sistema calcula diferenças do 13º salário na folha (Roteiro FOL) quando o mnemônico **P\_CCOMP13** está ativado. Essas diferenças podem ser médias, reajustes salariais e outros casos.

Se o **P\_CCOMP13** estiver ativado, o sistema vai calcular as diferenças no mesmo período em que a **parcela única do 13º** foi processada.  
Exemplo: Se a parcela única foi calculada em **novembro** e o mnemônico está ativado, então o sistema fará o cálculo das diferenças do 13º na folha de novembro, caso o funcionário tenha valores a receber.

Se **não quiser pagar diferenças do 13º antes de dezembro**, então deve **desativar o mnemônico** e ativá-lo somente em dezembro.   
O roteiro **132** deve ser criado em dezembro, e as diferenças serão calculadas no Roteiro FOL **após o fechamento do roteiro 132**.

**Para saber como gerar o 13º Salário Parcela Única pago em novembro, ao eSocial, clique** [**aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020111952-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-o-13%C2%BA-Sal%C3%A1rio-Parcela-%C3%9Anica-pago-em-novembro-conforme-Nota-Orientativa-10-2018?source=search)**.**  
  
Para auxiliar na conferência entre folha de pagamento e eSocial de BASE FGTS e FGTS recolhido, foram criados os Ids 1962 e 1963 para gravar o valor do FGTS 13º sobre o líquido, quando a segunda parcela do 13º for paga antes do mês de dezembro. Clique [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36695547122327-RH-Linha-Protheus-GPE-Novas-verbas-de-Base-FGTS-quando-a-2%C2%AA-parcela-do-13%C2%BA-for-paga-antes-do-m%C3%AAs-de-dezembro) para consultar o material.  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo da 1ª parcela do 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409855157399-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionadas-ao-c%C3%A1lculo-da-1%C2%AA-parcela-do-13-Sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionados ao cálculo da 2ª parcela do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409828940055-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionados-ao-c%C3%A1lculo-da-2%C2%AA-parcela-do-13%C2%BA-Sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Quais são as documentações relacionadas ao cálculo do complemento de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410720423959-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-documenta%C3%A7%C3%B5es-relacionadas-ao-c%C3%A1lculo-do-complemento-de-13%C2%BA)
