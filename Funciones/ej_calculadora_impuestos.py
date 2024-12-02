

def pago_impuesto(sin_impuesto,porcentaje):
    pago_total=sin_impuesto+sin_impuesto*(porcentaje/100)
    print(f'El pago con impuesto es de: {pago_total}')


sin_impuesto_us=int(input('Proporcione el pago sin impuesto:'))
porcentaje_us=int(input('Proporcione el porcentaje del impuesto:'))

pago_impuesto(sin_impuesto_us,porcentaje_us)