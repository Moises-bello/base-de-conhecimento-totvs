---
article_id: 360046498433
category: RH - MANAD
content_hash: 79413c4c75238255a0a611d5ddc874b249cac81e6d6038eafe0a5e5bdbd17759
fetched_at: '2026-06-28T22:43:33.829519+00:00'
product: protheus
section_id: 360008157193
source: central-protheus
title: RH - Linha Protheus - GPE - ERRO/AÇÃO na validação do arquivo MANAD no SVA
type: support-article
updated_at: '2023-09-05T17:53:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046498433-RH-Linha-Protheus-GPE-ERRO-A%C3%87%C3%83O-na-valida%C3%A7%C3%A3o-do-arquivo-MANAD-no-SVA
---

**Dúvida**ERRO/AÇÃO na validação do arquivo MANAD no SVA  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução:****1)** Erro: Arquivo não está no padrão MANAD ou a primeira linha de identificação é inválida **[MP - GPE - Erro na validação MANAD: Arquivo não está no padrão MANAD ou a primeira linha de identificação é inválida](https://totvssuporte.zendesk.com/knowledge/articles/360046402253/pt-br?brand_id=1509248)**

**2)** Erro: A versão informada no registro de abertura não é valida (001)Informar no processamento MANAD (Wizard) , tela do passo 1/7 no campo versão do layout = 03- INS MPS/SRP nº12/2006  
 **3)** Erro: Base de Cálculo do IRRF está divergente da soma das rubricas classificadas como 1 e 2;  
Documentação para correção:   
<https://tdn.totvs.com/display/public/PROT/GPEM110A+-+ERRO%3A+Base+de+calculo+IRRF+divergente+da+soma+das+rubricas+classificadas+como+1+e+2>  
  
 **4)** Erro: Remuneração em competência fora do período do contrato de trabalho;  
**Ação:** Analisar na linha do erro comparando com o pagamento nos acumulados se a remuneração é oriunda de rescisão complementar de dissídio ou comissão. Em caso afirmativo considerar como aviso. Em caso negativo , o fiscal poderá notificar a empresa observando que a rescisão complementar do tipo normal deve ser calculada na competência da rescisão principal.   
  
 **5)** Erro: CNPJ/CEI do estabelecimento não existente entre os registros de abertura (0000)  
**Ação:** Vide itens anteriores (cadastro do centro de custo atrelado aos funcionário e também se atentar se suas tabelas SI3 e CTT constam com os mesmos registros.  
  
 **6)** Erro: Duplicidade de registro (mesma chave de outro registro existente);

|  |  |
| --- | --- |
| **K250 ou K300 – Duplicidade de registro (mesma chave de outro registro existente).** | Verificar pela linha do erro, a matricula do funcionário e o mês a que se refere. Entrar no acumulado do funcionário (tabela SRD), e verificar uma possível divergência (duplicidade) nos valores. |

**7)** Erro: Valor de base de cálculo das contrib. prev. correspondente não localizada no registro K250;

|  |  |
| --- | --- |
| **K300 XXXXXX Erro Valor de base de cálculo das contrib. prev. correspondente não localizada no registro K250.** | Foi encontrada uma verba em um determinado centro de custo e na verba de base de INSS (id 0013 e id 0014) não foi encontrada a base de INSS para esta verba que esta em centro de custo diferente. Orientado ao cliente a localizar a linha do erro onde K300 CNPJ + C.C + Matricula + Verba + mês/ano + valor  devera ir no acumulado e verificar para cada matricula esta situação e fazer a correção necessária. |

**8)** Erro: TRABALHADOR não localizado no registro K050;  
Existe informação no bloco K300 , porém não há cadastro do trabalhador no bloco K050.   
Verificar no cadastro do funcionário o tipo de admissão ou se existe transferência. A data da transferência deve existir no histórico para o mesmo CNPJ que ele está atualmente. Verificar também se existe alguma data de demissão informada no cadastro.
