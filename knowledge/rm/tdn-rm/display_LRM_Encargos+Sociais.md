---
content_hash: a76328dc618c2f415178c58cdb7c130652c4ae34fb48e27dff96808a06eb40c0
fetched_at: '2026-06-29T00:10:07.328498+00:00'
page_id: '452719402'
product: rm
source: tdn-rm
title: Encargos Sociais
type: documentation
url: https://tdn.totvs.com/display/LRM/Encargos+Sociais
version: 28
---

Neste etapa será configurado algumas definições para o cálculo de encargo sociais.  
   
**Parâmetros**

Calcula salário maternidade conforme SEFIP

O parâmetro calcula salário maternidade conforme SEFIP, foi alterado para a página [Folha Normal / Salario Maternidade 1/2](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719554), para melhor posicionamento dos parâmetros.

   
Atualização de FGTS obrigatória  
Com este parâmetro marcado, obriga que seja feita a atualização do FGTS antes da Liberação de competência.  
   
Atualiza manutenção de FGTS  
   
Trunca valores de FGTS/INSS  
Com este parâmetro marcado, no cálculo do FGTS e nos relatórios o sistema irá desprezar os valores existentes a partir da segunda casa decimal.

É importante ressaltar que na folha analítica, este parâmetro irá influenciar no valor apresentado no campo FGTS Dep. (SEFIP)) onde demonstra os valores de FGTS.

Arredonda INSS teto quando funcionário possui outro vínculo de terceiros

Parâmetro para truncar ou arredondar o teto do INSS de acordo com o cálculo considerando o valor do evento de outro emprego lançado no movimento do funcionário.

Com o parâmetro DESmarcado - O sistema aplicará o truncamento para o valor de contribuição seguindo a regra utilizada pelo eSocial.

O cálculo do INSS considerará a informação de outras bases externas respeitando o teto do INSS vigente na competência.

Quando a soma das bases dos vínculos atinge o teto de contribuição do INSS, o sistema irá calcular e truncar os valores em cada faixa, de forma que a soma final da contribuição não ultrapasse o teto nem gere diferença com o valor validado pelo eSocial.

Com o parâmetro Marcado - O sistema aplicará o arredondamento para o valor de contribuição seguindo a regra utilizada pelo eSocial.

O cálculo do INSS considerará a informação de outras bases externas respeitando o teto do INSS vigente na competência.

Quando a soma das bases dos vínculos atinge o teto de contribuição do INSS, o sistema irá calcular e arredondar os valores em cada faixa, de forma que a soma final da contribuição não ultrapasse o teto nem gere diferença com o valor validado pelo eSocial.

Exemplo:

Dados Fictícios

Quando após o cálculo das faixas de contribuição na base de INSS Outro Emprego e a base de cálculo para INSS do salário inicia na 3ª faixa

Cálculo  = 1190,83 \* 0,12 = **142,8996**

PARÂMETRO DESMARCADO = 142,89

PARÂMETRO MARCADO = 142,90

 

Usa AAS discriminado  
Este parâmetro deverá será utilizado por usuários que emitem a relação de salários de contribuição com verbas discriminadas.   
   
Utiliza Controle de Compensação na Guia de INSS

Habilita Histórico de INSS no cadastro de seção  
Este parâmetro permite armazenar os percentuais de INSS empresa na geração da guia de INSS.

**Atenção:**

Quando este parâmetro estiver marcado, será habilitado no anexo do cadastro das seções o "Histórico de Percentuais para INSS" .

Maiores informações:  [Habilita Histórico de INSS no Cadastro de Seção.](https://tdn.totvs.com.br/pages/releaseview.action?pageId=496388652)

Discriminar Percentual de Terceiros

Ao marcar o parâmetro, será disponibilizada a aba **'Percentuais de Terceiros'** no menu Administração de Pessoal | Cadastros | Seções | Anexos | Histórico de Percentuais para INSS para que o usuário realize o cadastro dos percentuais de terceiros discriminados conforme Tabela de Códigos de Receita da DCTFWeb eSocial. Vale ressaltar que, nos casos em que não há recolhimento, como é comum em empresas filantrópicas isentas de determinados encargos, é fundamental preencher os percentuais com "0-zero".  Este procedimento assegura a precisão e a consistência no cálculo dos encargos. 

Percentual SEST/SENAT:

Este campo permite informar o percentual que o usuário deseja para calcular o percentual de terceiros para Autônomos.

Caso não seja preenchido o sistema irá considerar o percentual fixo de 2,5%.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[<<Voltar para tela anterior **Folha Normal**](http://tdn.totvs.com.br/display/LRM/Folha+Normal)
