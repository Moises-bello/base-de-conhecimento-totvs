---
article_id: 19253593564951
category: RH - 13º salário
content_hash: e6c73a06ff4d79133d1bc0dd59551389c6df211ea6d56fffdbd049c126ce9811
fetched_at: '2026-06-28T22:44:00.423349+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Ao processar o complemento da 1ª Parcela do 13º
  Salário, as diferenças dos adicionais não são separadas da verba de 13º Salário
  1ª Parcela
type: support-article
updated_at: '2026-06-25T11:10:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19253593564951-RH-Linha-Protheus-GPE-Ao-processar-o-complemento-da-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-as-diferen%C3%A7as-dos-adicionais-n%C3%A3o-s%C3%A3o-separadas-da-verba-de-13%C2%BA-Sal%C3%A1rio-1%C2%AA-Parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19253577678871) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Porque ao processar o complemento da 1ª parcela do 13º salário para funcionário que recebeu antecipação nas férias, as diferenças dos adicionais não são sseparadas da verba de 13º Salário 1ª Parcela (ID 0022)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Conforme observação no final da documentação abaixo, a separação dos IDs de 1ª parcela não se aplica para a antecipação do 13º salário nas férias pois anteriormente **já não havia desmembramento do cálculo.**

Nas férias **não temos a quebra de adicionais** e devido a isso, ao processar o cálculo do complemento da 1ª parcela do 13º salário, a diferença dos adicionais será contemplada na verba de 1ª parcela de 13º salário (id 0022).

* [Separação Adicionais Médias 1ª Parcela do 13º Salário](https://tdn.totvs.com/pages/releaseview.action?pageId=403745443)
* [Antecipação de 13º nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006362581-RH-Linha-Protheus-GPE-Como-antecipar-o-13%C2%BA-Salario-nas-f%C3%A9rias)

**Exemplo**  
Funcionário teve Antecipação do 13º Salário nas Férias, e posteriormente foi realizado Reajuste Salarial e Reajuste do valor do Adicional de Triênio.

1. Cálculo das Férias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34052745883031)  
  
Cálculo da Antecipação do 13º Salário nas Férias:

Salário: 6.400,00  
Triênio: 154,00  
Salário + Triênio x 50% = 3.277,00  
  
2. Cálculo do Complemento do 13º Salário:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19253625810455)  
  
Cálculo do Complemento do 13º Salário:  
Salário Reajustado: 6689,92  
Triênio Reajustado: 160,96  
Complemento 13º 50% = Salário + Triênio x 50% - Antecipação das Férias.  
  
6689,92 + 160,96 = 6.850,98  
6.850,98 x 50% = 3.425,44  
4.425,44 - 3.277,00 = **148,44**  
   
No complemento de 148,44, está sendo considerado 144,96 referente ao salário + 3,48 referente ao triênio. 

**Saiba Mais**[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)
