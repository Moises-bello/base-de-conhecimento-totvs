---
article_id: 115001380867
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: e372e26903db2a73d893ff94f454d048f16499578cce09c884dfc41054385c17
fetched_at: '2026-06-28T22:38:44.091530+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Nota de saída saindo com
  hora (F2_HORA) errada
type: support-article
updated_at: '2026-05-15T19:54:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001380867-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Nota-de-sa%C3%ADda-saindo-com-hora-F2-HORA-errada
---

**Ocorrência**  
O Campo F2\_HORA está sendo gravado com o horário incorreto, causando problemas de rejeições no momento da transmissão, como resolver?

**Causa**

Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e a data-hora de emissão (dhEmi) for maior que a data-hora da Sefaz, no momento do recebimento do documento, será retornado a rejeição "703 - Data-Hora de Emissão posterior ao horário  de recebimento".

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - a partir da versão 11.  
  
**Solução**  
  
Para solucionar a gravação do campo F2\_HORA na preparação do documento, ajuste o parâmetro **MV\_HORARMT:**

* **1** = Gravar na Nota o horário registrado na máquina em que está acessando o SmartClient;
* **2** = Gravar na nota a hora que está registrado no servidor onde está instalado o Protheus;
* **3** = Gravar na Nota o horário do servidor, mas adaptar ao fuso horário de cada Filial -> Esta opção é utilizada **APENAS** **para empresas que emitem em uma mesma máquina NFs para diversas Filiais, em que, uma possui fuso horário diferente da outra.** Nesta opção, é necessário também configurar os parâmetros **MV\_HVERAOI e MV\_HVERAOF** com início e fim do horário de verão, no formato americano de ano, mês e dia (20151018).

Mais detalhes sobre este assunto, acesse: [**FAT0147 - Horario de Verão campo F2\_HORA com hora incorreta (MV\_HORARMT, MV\_HVERAOI, MV\_HVERAOF, 1452cod703 e Rejeição 578 e703)**](http://tdn.totvs.com/pages/viewpage.action?pageId=267794836)

***Atenção***: Tendo realizado as devidas configurações, deve-se excluir o Documento de Saída e realizar novamente a rotina de Preparação de Documento de Saída, para então, gravar o campo **F2\_HORA** corretamente.

**Importante**: O campo F2\_EMISSAO também deve ser devidamente registrado.

**Observação**: Essa rejeição, durante o horário de verão brasileiro, ocorre com uma maior frequência, pois há mudança nos horários dos servidores das SEFAZ, todavia, desde o ano de 2019 não está mais sendo adotado o horário de Verão, conforme lei sancionada pelo presidente da república em exercício.

**SAIBA MAIS:**

[**MP - NFE - Como configurar o sistema para o Horário de Verão ?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013529028-MP-NFE-Como-configurar-o-sistema-para-o-Hor%C3%A1rio-de-Ver%C3%A3o-)

[**MP - NFE - 703 - Data-Hora de Emissão posterior ao horário de recebimento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018266352-MP-NFE-703-Data-Hora-de-Emiss%C3%A3o-posterior-ao-hor%C3%A1rio-de-recebimento-)

[**MP -NFE - Rejeição: 578 - A data do evento não pode ser maior que a data do processamento?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018844451--MP-NFE-Rejei%C3%A7%C3%A3o-578-A-data-do-evento-n%C3%A3o-pode-ser-maior-que-a-data-do-processamento-)

[**MP-FAT-Os parâmetros MV\_HVERAOI e MV\_HVERAOF devem ser alterados manualmente todo ano**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018606391-MP-FAT-Os-par%C3%A2metros-MV-HVERAOI-e-MV-HVERAOF-devem-ser-alterados-manualmente-todo-ano)

[**MP-FAT-Término do horário de Verão**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022631391-MP-FAT-T%C3%A9rmino-do-hor%C3%A1rio-de-Ver%C3%A3o)
