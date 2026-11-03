---
content_hash: f3a8afa04e31b0f9bcb27b5f243d65381f8e71276368ffba4673111ed2dc851f
fetched_at: '2026-06-29T00:10:10.449730+00:00'
page_id: '452719842'
product: rm
source: tdn-rm
title: Dados da Pensão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719842
version: 3
---

Dados da Pensão são dados para o cálculo do desconto da pensão alimentícia do funcionário.  
   
**Observação:**  
1.     Para o lançamento da pensão alimentícia para um funcionário, através de fórmula:  
(SM\* 56%)   
O sistema calcula da seguinte forma:  
Calcula a fórmula (SM\*0.5

6) = R$ 100,80 e aplica o percentual informado no cadastro que deve ser **100%**.   
2.     Cadastre em Tabelas dinâmicas (Tabela INT 45) o Tipo de Pensão. Este campo é meramente informativo para o controle do usuário.  
3.     A fórmula de cálculo da pensão alimentícia terá prioridade sobre os outros tipos de cálculos realizados através dos dados da pensão.  
   
Sugestão de fórmula para cálculo de pensão sobre o rendimento líquido mensal:  
   
DECL VALOR,CONT;   
DECL RB, CP, PERC;  
SETVAR (RB, NDEPBRUTO (NDEPCORRENTE) );   
SETVAR (CP, TI(A('01')));  
SETVAR (PERC, TABDEP('PERCENTUAL' , 'V', NDEPCORRENTE) / 100 );   
REPITA   
SETVAR (VALOR, PERC \* (RB - CP - TR (RB - CP - VALOR) ) );   
SETVAR (CONT, CONT+1)  
ATE CONT = 7;  
SE PERC > 0 ENTAO  
VALOR / PERC   
SENAO  
0  
FIMSE  
   
4.    È possível somar um valor ao cálculo da pensão cadastrando uma Fórmula adicional de pensão.  
   
5.    O lançamento financeiro da pensão alimentícia será gerado com o fornecedor registrado neste campo caso as seguintes opções estejam marcadas: Opção "Usar definição da parametrização" do grupo "Lançamentos Individuais" na Geração de Lançamentos Financeiros e a Opção "Dependente" do grupo "Origem do fornecedor" na Parametrização dos Lançamentos Financeiros.  
   
**Observação:**  
Em caso de a coligada possuir licença de uso do Sistema de Controle Financeiro RM Fluxus e nos parâmetros do RM Fluxus, item "Parâmetros Lançamentos", estiver desmarcado o parâmetro "Permite Globais", não será possível associar em campos de cadastros do RM Labore, Cliente/Fornecedor que foram cadastrados como "Global".

**Possui Retenção FGTS**

Ao marcar esse parâmetro o sistema passa a gerar as informações das tag's pensAlim,percAliment e vrAlim nos eventos S-2299 e S-2399, conforme os dados da pensão cadastrados.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários

Dependentes
