---
article_id: 40453134437015
category: Ativo Fixo - EFD Contribuições - Registros F120/F130
content_hash: dbcec42662a37fd67a768a7d68913ca5c76d3a146be55b62d29f16e8564a47ee
fetched_at: '2026-06-28T22:41:36.227901+00:00'
product: protheus
section_id: 31045161075991
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - Diferença na
  geração dos registros F120 e F130 no EFD Contribuições
type: support-article
updated_at: '2026-05-14T23:32:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40453134437015-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-Diferen%C3%A7a-na-gera%C3%A7%C3%A3o-dos-registros-F120-e-F130-no-EFD-Contribui%C3%A7%C3%B5es
---

Os registros F120 e F130 no EFD Contribuições diferem na base do crédito do ativo imobilizado: F120 calcula sobre a depreciação mensal, enquanto F130 sobre o valor de aquisição do bem. No módulo SIGAATF, é essencial validar o cadastro de ativos e o tipo de crédito para garantir a geração correta dos registros, além de configurar adequadamente o CST de PIS/COFINS e os parâmetros no SIGAFIS.

**Dúvida**  
Qual a diferença entre os registros F120 e F130 na geração do EFD Contribuições e quais as premissas para que o sistema gere as informações corretamente no módulo SIGAATF?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - A partir da Versão 12.1.2410

**Solução**  
A geração dos registros F120 e F130 no EFD Contribuições dentro do Protheus baseia-se na origem do crédito do ativo imobilizado. A principal diferença reside no fato de o crédito ser calculado sobre o valor da depreciação mensal (F120) ou sobre o valor de aquisição do bem (F130).

1. **Registro F120 (Bens Incorporados ao Ativo Imobilizado - Depreciação/Amortização):** Este registro é destinado aos créditos calculados com base nos encargos de depreciação ou amortização do mês. O sistema considerará o bem enquanto houver base de cálculo de depreciação, ou seja, até que o bem esteja totalmente depreciado ou sua base de cálculo seja zerada.
2. **Registro F130 (Bens Incorporados ao Ativo Imobilizado - Aquisição):** este registro é utilizado quando o crédito é apropriado com base no valor de aquisição do bem. Diferente do F120, ele foca na operação de compra e classificação, em que o aproveitamento do crédito ocorre conforme a legislação vigente para aquisições.

Para garantir a fidelidade das informações e a correta geração dos registros, valide os seguintes cadastros e parametrizações:

1. Acesse o módulo **SIGAATF** e verifique o **Cadastro de Ativos (ATFA012)**.
2. Certifique-se de que o campo **Tipo de Crédito (N1\_TPCRED)** está preenchido corretamente:

   * Para o **F120**, o sistema valida bens que geram encargos de depreciação.
   * Para o **F130**, o sistema valida a base de aquisição.
3. No módulo **SIGAFIS**, valide os parâmetros da Wizard de geração do EFD Contribuições, garantindo que a apuração de PIS/COFINS esteja configurada para ler os dados do Ativo Imobilizado.
4. Verifique se o bem possui o campo **CST de PIS/COFINS** preenchido adequadamente nas notas de entrada ou no cadastro do ativo, pois isso determina a elegibilidade ao crédito.

**Saiba Mais**  
[Como gerar o Registro F120 EFD Contribuições](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016151811-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-Registro-F120-EFD-Contribui%C3%A7%C3%B5es)  
[Como gerar o registro F130 EFD Contribuições](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016728011-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-F130-EFD-Contribui%C3%A7%C3%B5es)
