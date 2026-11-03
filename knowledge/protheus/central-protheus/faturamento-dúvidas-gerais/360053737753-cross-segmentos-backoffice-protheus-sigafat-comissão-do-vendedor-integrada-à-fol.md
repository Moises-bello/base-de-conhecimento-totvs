---
article_id: 360053737753
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 6fcf946c5cc2f51af9577b98ad332ed4020445adbbe58cff33920bc99950a125
fetched_at: '2026-06-28T22:38:28.799645+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Comissão do Vendedor integrada
  à Folha de Pagamento
type: support-article
updated_at: '2026-04-02T11:35:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053737753-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Comiss%C3%A3o-do-Vendedor-integrada-%C3%A0-Folha-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39468783724951)Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como gerar a comissão do vendedor (**MATA040**) integrada a folha de pagamento no Recursos Humanos?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

**1.** Cadastrar **funcionário** no módulo Gestão de pessoal.

**2.** Cadastrar vendedor no módulo Faturamento informando a forma de pagamento (**A3\_GERASE2**) = Folha de Pagamento; e no campo "Funcionário" informe a matrícula do funcionário relacionado ao Vendedor, para que seja gerado o provento de comissão na folha de pagamento (no ambiente Gestão de Pessoal).

**3.** Ao rodar a rotina **MATA530** - "Atualiza Comissão de Pagamento" deve atentar-se a todos os parâmetros que delimitam o cálculo de comissões. Inclusive o parâmetro "Habilita interface pagamento? = Sim". A comissão gerada pode ser observada na rotina **MATA490** - Manutenção de comissões. As considerações para o valor calculado de comissão, para o **E3\_BASE** podem ser verificadas na FAQ**:**[**FAT0052\_Configuração\_Das\_Comissões\_Dos\_Vendedores**](https://tdn.totvs.com/pages/viewpage.action?pageId=235598457)

**4.** No módulo de gestão de pessoal deve constar a Verba de Pagamento - Tabela **SRV**, com todos os códigos de identificação de cálculo, e no cadastro da verba de pagamento de comissão o campo **RV\_CODFOL** deve ter o código de **Verba 165 / 179 (comissões)** vinculado à Tabela (Obs: Caso no campo **RV\_CODFOL** não tenha a opção de selecionar a tabela 35 de códigos de identificadores de cálculo; ou ***havendo outras dúvidas sobre os códigos das verbas, entrar em contato com o suporte Protheus GPE***), e o campo **RV\_TIPOCOD** = provento. Efetuando estes passos irá gerar informações na tabela **SRK**.  
  
A verba 1882 deve estar cadastrada também, conforme documentação: [RH - Linha Protheus - GPE - Criação ID 1882 no cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414658799383-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-ID-1882-no-c%C3%A1lculo-de-f%C3%A9rias?source=search)  
  
Caso a comissão seja calculada On-Line, o sistema vai gerar a **SE3** e não vai gerar a **SRK**. Somente após rodar o **MATA530** será preenchido o campo **E3\_DATA** e a tabela **SRK** será preenchida  
  
Cada vez que o **MATA530** for rodado, o sistema vai gerar uma linha na **SRK** aglutinando valores da **SE3**, porém, não vai aglutinar valores em uma linha quando a rotina for rodada diversas vezes

|  |
| --- |
| Assista ao vídeo explicativo para entender o fluxo de cadastro e comissão no Faturamento:  [How To | MP - SIGAFAT - Configuração de vendedor para comissões](https://www.youtube.com/watch?v=hxKM-ESpAKI) |

**Saiba Mais**:  
[**FAT0120\_Comissão\_integrada\_à\_Folha\_de\_Pagamento**](https://tdn.totvs.com/x/o3yZDg)

[**MP-FAT-Comissão-Zerada**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020902012-MP-FAT-Comiss%C3%A3o-Zerada)

[**MP-FAT-Como-alterar-comissão-de-venda**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007526581-MP-FAT-Como-alterar-comiss%C3%A3o-de-venda)

[**MP-FAT-Como-gerar-comissão-do-Cadastro-do-Cliente-**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028132651-MP-FAT-Como-gerar-comiss%C3%A3o-do-Cadastro-do-Cliente-)
