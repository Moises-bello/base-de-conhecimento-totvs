---
content_hash: 68a1b14350b999e1bd749aade2fe806d46461bdc8b5b71f5c9dfa49fd1756269
fetched_at: '2026-06-29T00:06:29.703248+00:00'
page_id: '234616121'
product: rm
source: tdn-rm
title: TUMLE8_DT_Contribuicao_Sindical_Afastado_Retorno_Mes
type: documentation
url: https://tdn.totvs.com/display/LRM/TUMLE8_DT_Contribuicao_Sindical_Afastado_Retorno_Mes
version: 2
---

# CONTRIBUIÇÃO SINDICAL DE AFASTADO RETORNANDO NO MÊS DE MARÇO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Contribuição Sindical* |
| **Situação/Requisito:** | *No cálculo da Contribuição Sindical, CC 12, existe um tratamento para atender à legislação abaixo, sobre funcionários com retorno de afastamentos no mês.*  *Neste caso o desconto é feito no mês subsequente.*  *"CLT - Decreto Lei nº 5.452 de 01 de Maio de 1943*  *Aprova a Consolidação das Leis do Trabalho.*  *Art. 602 - Os empregados que não estiverem trabalhando no mês destinado ao desconto do imposto sindical serão descontados no primeiro mês subsequente ao do reinício do trabalho. (Vide Lei nº 11.648, de 2008)*  *Parágrafo único - De igual forma se procederá com os empregados que forem admitidos depois daquela data e que não tenham trabalhado anteriormente nem apresentado a respectiva quitação."*  *Entretanto, existem textos, como o do link <http://www.iob.com.br/noticiadb.asp?area=trab_prev&noticia=113080>, que dá a entender que para retorno de afastamentos até o mês de março, se houve percepção de salário, o desconto pode ser efetuado no próprio mês.* |
| **Solução/Implementação:** | *Alterar a regra da Contribuição Sindical de afastados, para efetuar o desconto no mês subsequente ao do reinício do trabalho, somente em retorno de afastamentos à partir da competência abril.*  *Para retornos nos meses de janeiro, fevereiro ou março, o desconto será efetuado na competência março, assim como os demais funcionários.* |
| **Chamados   relacionados:** | *TUMLE8, TUMVS2, TUMFNQ, TUNBB8* |
| **Versões/Release:** | *11.82.43, 12.1.10* |
