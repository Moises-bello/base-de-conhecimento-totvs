---
article_id: 360019893271
category: GPE - eSocial - Periódicos
content_hash: 12cd54b5f0813bb9f668579c0a0c7e4b53ab4e7b3ffaa2c5c31f6712703f9908
fetched_at: '2026-06-28T22:45:08.708845+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Para as informações do 13º salário
  deve ser enviado para o governo a 1º parcela com a natureza de rubrica 5504 e a
  2º parcela com a natureza 5001, como separar as verbas de adicionais e médias no
  sistema
type: support-article
updated_at: '2025-07-21T14:15:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019893271-RH-Linha-Protheus-GPE-eSocial-S-1200-Para-as-informa%C3%A7%C3%B5es-do-13%C2%BA-sal%C3%A1rio-deve-ser-enviado-para-o-governo-a-1%C2%BA-parcela-com-a-natureza-de-rubrica-5504-e-a-2%C2%BA-parcela-com-a-natureza-5001-como-separar-as-verbas-de-adicionais-e-m%C3%A9dias-no-sistema
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19414553777303) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Para as informações do 13º salário deve ser enviado para o governo a primeira parcela com a natureza de rubrica **5504** e a segunda parcela com a natureza **5001**, como separar as verbas de adicionais e médias no sistema?  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19414540753815)  
Fonte: [Tabela 03 do leiaute eSocial - Natureza das Rubricas da Folha de Pagamento](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/tabelas.html#03)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Devido as naturezas e incidências de **INSS e IRRF** serem diferentes da primeira e segunda parcela, foram liberadas para a criação de novos **IDs de cálculos** a serem vinculados nas Verbas de Adicionais e Médias de 13º Salario primeira parcela.  
  
Desta forma as verbas de adicionais (como **Periculosidade**, **Insalubridade**, **Adicional de Confiança)** e **médias** pagas no 13º salário, ficarão separadas em primeira e segunda parcela.  
  
Nos links abaixo é possível acessar a documentação e pacotes para criação dos novos Ids.  
  
***Links*:**

* [RH - Linha Protheus - GPE - Separação Adicionais e Médias 2ª Parcela do 13º Salário Maternidade (Criação IDs de cálculo 1434 ao 1447 e IDs 1651 a 1652)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10008359545879)
* [RH - Linha Protheus - GPE - Separação Adicionais e Médias 1ª Parcela do 13º Salário Maternidade (Criação IDs de cálculo 1639 ao 1648 e IDs 1653 a 1654)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454112)
* [RH - Linha Protheus - GPE - Separação dos Adicionais e Médias da 1ª Parcela do 13º Salário (Criação IDs de cálculo 1628 ao 1637)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016051891-MP-GPE-Separa%C3%A7%C3%A3o-dos-Adicionais-e-das-M%C3%A9dias-da-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-Cria%C3%A7%C3%A3o-IDs-de-c%C3%A1lculo-1628-ao-1637-?source=search)

**Atenção:** Os Usuários que processaram a folha de 1º Parcela de 13º salário após esta atualização ou ainda não efetuaram o cálculo: **não é necessário executar os passos abaixo**.  
  
Na ocasião, foi orientado para os usuários, que já haviam pago a primeira parcela, que executassem o **RDMAKE UPDVB131,** esse RDMAKE altera os códigos das verbas de 1º parcela de 13º na SRD.  
  
Porém, caso os valores de Adiantamento de 13º que já tenham sido enviados para o RET com os códigos de verbas antigo, é necessário, além de corrigir a tabela SRD,  retificar os eventos S-1200/S-1210, na situação em que a DCTFWeb tenha efetuado o cálculo do INSS, no mês do adiantamento, considerando a Base de Cálculo de 13º Salário.  
  
Documentação Técnica: <https://tdn.totvs.com/x/mA4QGg>  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Novos IDs Folha](http://tdn.totvs.com/x/L40OFQ)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
