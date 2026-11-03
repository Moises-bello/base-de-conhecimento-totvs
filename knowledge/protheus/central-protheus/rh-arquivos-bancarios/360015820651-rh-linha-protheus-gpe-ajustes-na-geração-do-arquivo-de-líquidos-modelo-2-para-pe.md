---
article_id: 360015820651
category: RH - Arquivos Bancarios
content_hash: 7a679a1714a874f7087459ad0009e99c67ab6a68f7e6db76851ed3b2dc9b845c
fetched_at: '2026-06-28T22:43:38.240354+00:00'
product: protheus
section_id: 360004833673
source: central-protheus
title: RH - Linha Protheus - GPE - Ajustes na geração do arquivo de Líquidos Modelo
  2 para permitir quebrar ou não pelo Tipo de Conta
type: support-article
updated_at: '2026-06-25T20:15:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015820651-RH-Linha-Protheus-GPE-Ajustes-na-gera%C3%A7%C3%A3o-do-arquivo-de-L%C3%ADquidos-Modelo-2-para-permitir-quebrar-ou-n%C3%A3o-pelo-Tipo-de-Conta
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32326007609111)**Tempo aproximado para leitura:**00:02:00 min**

**Ocorrência**  
No módulo Gestão de Pessoal foi implementada na versão 12 uma melhoria que tornou possível a geração do arquivo de Líquidos para Múltiplos Lotes.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Contudo, a partir dessa melhoria o sistema passou a agrupar os funcionários ordenados pelo **Código do Banco** + **Tipo da Conta Salário**. No caso, o Tipo da Conta pode ser Poupança ou Conta Corrente, e após a geração de um desses grupos ocorria uma quebra com o seu total respectivo.   
Por isso, visando flexibilizar essa funcionalidade, estamos disponibilizando o campo "**Quebra Tipo Conta** **(S/N)**" na Tabela **S052 - Parâmetros para CNAB/SISPAG**, o qual será possível definir se haverá ou não a quebra pelo Tipo de Conta. Defina com valor "S" os bancos que deseja que ocorra a quebra pelo Tipo de Conta, ou com valor "N" caso deseje que não ocorra a quebra.  
  
**Solução**  
Primeiramente será necessário estar com o sistema devidamente atualizado, para isso acesse o link a seguir para selecionar o pacote acumulado da sua release: [Pacote Acumulado RH.](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)

Procedimentos para o cálculo: Na rotina de **Manutenção de Tabela - GPEA320**, que pode ser localizada acessando no menu **Atualizações** / **Definições de Cálculo**, efetue a busca pela tabela **S052 - Parâmetros para CNAB/SISPAG**.   
Altere o novo campo "**Quebra Tipo Conta** **(S/N)**", informando S para os códigos dos bancos que deseja realizar a quebra pelo Tipo de Conta. Se esse campo ficar com valor N ou sem nenhum dado informado (vazio), o sistema irá realizar a quebra pelo Tipo de Conta de forma padrão.

**Saiba Mais**  
[RH - Arquivos Bancários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833673-RH-Arquivos-Bancarios)  
[CNAB - Valores Liquidos Multiplos Lotes](http://tdn.totvs.com/display/PROT/TVLNVO_DT_Geracao_CNAB_Valores_Liquidos_Multiplos_Lotes)
